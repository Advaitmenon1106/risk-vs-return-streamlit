import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from statsmodels.formula.api import ols
import datetime

country = st.selectbox('Choose a market', ['India', 'US [Work in Progress]'])

if country == 'India':
    col1, col2 = st.columns(2)

    tickers = pd.read_csv('./IndianTickers.csv')
    codes = tickers['YahooEquiv']
    names = tickers['NAME OF COMPANY']
    names_mapped = dict(zip(codes, names))

    valid_freq_codes = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    valid_freq_names = ['1 Day', '5 Days', '1 Month', '3 months', '6 months', '1 Year', '2 Years', '5 Years', '10 Years', 'Year-To-Date', 'Maximum']
    freq_mapped = dict(zip(valid_freq_names, valid_freq_codes))



    with col1:
        common_name_of_stock = st.selectbox('Choose a ticker', names)

    with col2:
        freq_name = st.selectbox('Choose a frequency', valid_freq_names)
        freq_code = freq_mapped[freq_name]


    target_ticker = [key for key, val in names_mapped.items() if val==common_name_of_stock][0]

    try:
        target_stock_data = yf.Ticker(target_ticker).history(freq_code)

        if target_stock_data.shape[0] == 0:
            st.write('Ticker not available on Yahoo Finance. Apologies for the inconvenience!')
        else: 
            st.write(target_stock_data)

    except:
        st.write('Ticker not available on Yahoo Finance or you may not have a stable internet connection. Apologies for the inconvenience!')