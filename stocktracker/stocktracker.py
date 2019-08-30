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
#  Usage limit: up to 5 API requests per minute and 500 requests per day
# -----------------------------------

import click
import requests
import configparser
import sys

config = configparser.ConfigParser()
config.read("config.ini")

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('symbs', nargs=-1, required=True)
@click.option('--alphabetize', '-a', is_flag=True, help="Alphabetize results, if flag provided")
def quote(symbs, alphabetize):
    """
    SYMBS - the symbols for which to fetch stock information. At least one is required. Enter up to 5 symbols at once.
    """
    key = config['DEFAULT']['ALPHA_VANTAGE_API_KEY']
    errors = []
    results = []
    count = 0
    latest_date = ""
    for symb in symbs:
    
        if count >= 5:
            print("Warning: processing only the first five symbols")
            break 
            
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symb}&apikey={key}"
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("An error occurred while fetching {}: ".format(url), e)
            sys.exit(1)
        
        if "Error Message" in response.json():
            errors.append("Unable to get data for symbol '{}'. Check that the symbol is correct.".format(symb))
            continue
        
        data = response.json().get("Time Series (Daily)")
        if data:
            count += 1
            latest_date = next(iter(data.keys()))
            latest_info = data.get(latest_date)
            results.append((symb.upper(), latest_info.get("4. close")))
        else:
            print("No data at this time (you may have reached the time limit for this service - up to 5 stocks per minute). Try again in a few seconds.".format(symb))
            sys.exit(0)
        
    if results:
        if alphabetize:
            results.sort()
        
        print("\nHere are the stock prices on {}:\n".format(latest_date))
        print("{:^10} {:^15}".format("Stock", "Quote"))
        print("{:=^25}".format("="))
        for symb, quote in results:
            print("{:^10} {:>12}".format(symb, quote))
        print("\n")
        
    if errors:        
        print("\n".join(errors))
        print("\n")