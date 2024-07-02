import psycopg2 as psg
import pandas as pd

from Daily_TBill_Scraping import get_todays_rf
conn = psg.connect('dbname = indian_tbill_data', user='postgres', password='supes@123')

with conn:
    with conn.cursor() as curs:
        vals = get_todays_rf()
        curs.execute('INSERT INTO tbill_data (date, yield) VALUES (%s, %s)', vals)
        conn.close()