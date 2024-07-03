import psycopg2 as psg
import pandas as pd
import streamlit as st

from Daily_TBill_Scraping import get_todays_rf
conn = psg.connect(dbname= st.secrets['db_name'], user=st.secrets['db_username'], password=st.secrets['db_password'])

with conn:
    with conn.cursor() as curs:
        vals = get_todays_rf()
        curs.execute('INSERT INTO tbill_data (date, yield) VALUES (%s, %s)', vals)
        
conn.close()