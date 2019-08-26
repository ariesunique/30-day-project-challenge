# -----------------------------------
# 4/1/2019
# 
# command-line tool to check the price of a given stock symbol
#
#  Psuedocode:
#    Read the parameters from the command line (uses Click module)
#    For each given stock symbol
#       Hit a service to get information about that stock
#       Read the response and extract data
#       Store the data in a list
#    Format the list and return to user
#
#  Use AlphaVantage service to get the stock quotes
#  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo
# -----------------------------------

import click
import requests
import configparser
import sys
from pprint import pprint

config = configparser.ConfigParser()
config.read("config.ini")

@click.command()
@click.argument('symbs', nargs=-1, required=True)
def quote(symbs):
    """
    SYMBS - the symbols for which to fetch stock information. At least one is required. Enter up to 5 symbols at once.
    """
    key = config['DEFAULT']['ALPHA_VANTAGE_API_KEY']
    errors = []
    count = 0
    for symb in symbs:
        #print(symb, count)
        if count > 5:
            print("Warning: processing only the first five symbols")
            break 
            
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symb}&apikey={key}"
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("An error occurred while fetching {}: ".format(url), e)
            sys.exit(1)
        
        if "Error Message" in response.json():
            errors.append("Unable to get data for symbol {}".format(symb))
            continue
        
        data = response.json().get("Time Series (Daily)")
        if data:
            count += 1
            latest_date = next(iter(data.keys()))
            latest_info = data.get(latest_date)
            print("On {}, the closing price of {} was ${}.".format(latest_date, symb, latest_info.get("4. close")))
        else:
            errors.append("No data for {}".format(symb))
            #pprint(data)

    if errors:        
        print("\n".join(errors))