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

@click.command()
def quote():
    click.echo("Stock quote goes here")