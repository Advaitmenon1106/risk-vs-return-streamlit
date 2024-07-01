import streamlit as st
import re
import numpy as np
import pandas as pd
import yfinance as yf
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
from datetime import timedelta as tdel, datetime as dt
from dateutil.relativedelta import relativedelta as rdel

from QueryDB import Query_DB

country = st.selectbox('Choose a market', ['India', 'US [Work in Progress]'])

if country == 'India':
    col1, col2 = st.columns(2)

    tickers = pd.read_csv('./IndianTickers.csv')
    codes = tickers['YahooEquiv']
    names = tickers['NAME OF COMPANY']
    names_mapped = dict(zip(codes, names))

    valid_freq_codes = ['1mo', '3mo', '6mo', '1y', '2y', '5y', '10y']
    valid_freq_names = ['1 month', '3 months', '6 months', '1 year', '2 years', '5 years', '10 years']
    freq_mapped = dict(zip(valid_freq_names, valid_freq_codes))

    with col1:
        common_name_of_stock = st.selectbox('Choose a ticker', names)

    with col2:
        freq_name = st.selectbox('Choose a frequency', valid_freq_names)
        freq_code = freq_mapped[freq_name]
        no_of_periods = int(re.search(r'\d+', freq_name).group())

        if 'Days' in freq_name:
            starting_date = dt.today()-rdel(days=no_of_periods)
        elif 'month' in freq_name:
            starting_date = dt.today()-rdel(months=no_of_periods)
        elif 'year' in freq_name:
            starting_date = dt.today()-rdel(years=no_of_periods)
        
        starting_date = starting_date.date()

    target_ticker = [key for key, val in names_mapped.items() if val==common_name_of_stock][0]

    try:
        target_stock_data = yf.Ticker(target_ticker).history(freq_code)
        if target_stock_data.shape[0] == 0:
            st.write('Ticker not available on Yahoo Finance. Apologies for the inconvenience!')
        else: 
            target_stock_data = yf.Ticker(target_ticker).history(freq_code)

    except:
        st.write('Ticker not available on Yahoo Finance or you may not have a stable internet connection. Apologies for the inconvenience!')
    
    nifty = yf.Ticker('^NSEI').history(freq_code)

    common_dates = nifty.index.intersection(target_stock_data.index)
    
    nifty = nifty.loc[common_dates]
    target_stock_data = target_stock_data.loc[common_dates]

    nifty_close = nifty['Close']
    target_stock_close = target_stock_data['Close']

    nifty_rtns = nifty_close.pct_change().dropna().to_numpy()
    target_stock_rtns = target_stock_close.pct_change().dropna().to_numpy()

    model = LinearRegression(fit_intercept=False).fit(X=nifty_rtns.reshape(-1, 1), y=target_stock_rtns)
    beta = model.coef_
    ytms = np.array(Query_DB(starting_date))
    Rf = ytms.mean()

    expected_return = Rf + beta*(nifty_rtns.mean()*100-Rf)
    
    st.write(pd.DataFrame({'Expected Return': expected_return, 'Mean of the stock return': target_stock_rtns.mean()*100, 'Risk free rate used': Rf, 'Beta of the stock': beta, 'Expected Market Return': nifty_rtns.mean()*100}))
    
    