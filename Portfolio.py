import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf

def list_potential_portfolios():
    portfolios_list = []

    tickers = pd.read_csv('./IndianTickers.csv')
    codes = tickers['YahooEquiv'].values
    names = tickers['NAME OF COMPANY'].values
    names_mapped = dict(zip(codes, names))

    symbols = list(names_mapped.keys())

    for i in range(0, len(symbols)):
        sym1 = symbols[i]
        stock1 = yf.Ticker(sym1).history('2y')
        
        for j in range(i+1, len(symbols)):
            sym2 = symbols[j]
            stock2 = yf.Ticker(sym2).history('2y')

            common_dates = stock1.index.intersection(stock2.index)

            rtns1 = stock1['Close'].loc[common_dates].pct_change().dropna().to_numpy()
            rtns2 = stock2['Close'].loc[common_dates].pct_change().dropna().to_numpy()

            corr = np.corrcoef(rtns1, rtns2)
            if corr[0, 1]<0:
                portfolio = f'{sym1} - {sym2}'
                st.write(portfolio)
                portfolios_list.append(portfolio)
    
    st.selectbox('Choose a portfolio', portfolios_list)
