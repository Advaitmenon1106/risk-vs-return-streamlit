import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf


def list_potential_portfolios():
    indian_tickers = pd.read_csv('./IndianTickers.csv')
    portfolios_list = []

    tickers = pd.read_csv('./IndianTickers.csv')
    codes = tickers['YahooEquiv'].values
    names = tickers['NAME OF COMPANY'].values
    names_mapped = dict(zip(codes, names))

    symbols = list(names_mapped.keys())

    for i in range(0, len(symbols)):
        sym1 = symbols[i]
        rtns1 = yf.Ticker(sym1).history('2y')['Close'].pct_change().to_numpy()
        for j in range(0, len(symbols)):
            sym2 = symbols[j]
            rtns2 = yf.Ticker(sym2).history('2y')['Close'].pct_change().to_numpy()
            corr = np.corrcoef(rtns1, rtns2)
            st.write(corr)
            if corr<0:
                portfolio = f'{sym1} - {sym2}'
                portfolios_list.append(portfolio)
    
    st.selectbox('Choose a portfolio', portfolios_list)

