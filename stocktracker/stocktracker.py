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

config = configparser.ConfigParser()
config.read("config.ini")

@click.command()
@click.argument('symbs', nargs=-1)
def quote(symbs):
    key = config['DEFAULT']['ALPHA_VANTAGE_API_KEY']
    for symb in symbs:
        click.echo(f"Getting stock information for {symb}")
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symb}&apikey={key}"
        response = requests.get(url)
        data = response.json()["Time Series (Daily)"]
        print(next(iter(data.values())))

