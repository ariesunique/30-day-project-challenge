# 30-day-project-challenge

Goal is to work on a project for a consecutive number of days, with 30 being the longest (so as not to get stuck in a rut - the idea is for these projects to be sprints, not marathons).

## stocktracker

This is a command-line script to retreive the latest stock quote for a given symbol. 

Example Usage:

    >> stocktracker GOOG
    
    Here are the stock prices on 2019-08-29:

    Stock      Quote
    =========================
    GOOG       1192.8500
    
To Install:
Note - This script uses [AlphaVantage](https://www.alphavantage.co/) API to get the latest stock quote. To run this code, you will need to sign up for a [free API key](https://www.alphavantage.co/support/#api-key).

1. Get your free API key from AlphaVantage (see above).
2. Clone this repository.
3. Rename or copy *config.ini.example* to *config.ini*. Replace the text "GET YOUR OWN KEY" with your AlphaVantage API key.
4. Install the project by running

         pip install --editable .


Note: If you are using a machine where you do not have write access to the default dir to install packages, then do the following:
1. mkdir ~/site-packages     
2. export PYTHONPATH='~/site-packages'
3. pip install --target ~/site-packages --editable .

Additional Note: If python3 is not your default python version, then use pip3 instead of pip. 
