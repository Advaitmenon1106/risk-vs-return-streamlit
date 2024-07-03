import pandas as pd
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = f"mongodb+srv://{st.secrets['mongo_username']}:{st.secrets['mongo_pw']}@cluster0.xhu6g0i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

tbill_db = client['tbill_data']
indian_tbill_data = tbill_db['indian_tbill_data']

df = pd.read_csv('./TBill-10Y.csv')
df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")
df.set_index('Date', inplace=True)

observations = []

for i in range (len(df.index)):
    date_to_be_inserted = df.index[i]
    yield_to_be_inserted = df.loc[date_to_be_inserted]
    observations.append({'Date': date_to_be_inserted, 'Yield': float(yield_to_be_inserted.values)})

indian_tbill_data.insert_many(observations)