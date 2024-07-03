import psycopg2 as psg
import pandas as pd
import streamlit as st
conn = psg.connect('dbname = indian_tbill_data', user=st.secrets['db_username'], password=st.secrets['db_password'])

with conn:
    with conn.cursor() as curs:
        curs.execute('CREATE TABLE tbill_data (date DATE NOT NULL PRIMARY KEY, yield NUMERIC)')
        df = pd.read_csv('./TBill-10Y.csv')
        df.set_index('Date', inplace=True)

        for i in range(0, len(df.index)):
            date_to_be_added = list(df.index)[i]
            ytm_to_be_added = df.loc[date_to_be_added]

            curs.execute('INSERT INTO tbill_data (date, yield) VALUES (%s, %s)', (date_to_be_added, float(ytm_to_be_added.values)))
