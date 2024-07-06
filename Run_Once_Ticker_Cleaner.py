import numpy as np
import pandas as pd
import yfinance as yf

indian_tickers = pd.read_csv('./IndianTickers.csv')
indian_tickers.set_index('YahooEquiv', inplace=True)
non_empty_stocks = []

codes = indian_tickers.index
names = indian_tickers['NAME OF COMPANY'].values
names_mapped = dict(zip(codes, names))

symbols = list(names_mapped.keys())

for i in range(0, len(symbols)):
    sym = symbols[i]
    stock = yf.Ticker(sym).history('2y')

    if stock.shape[0] != 0:
        indian_tickers.drop(sym, inplace=True)

indian_tickers.to_csv('./Output.csv')