from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import streamlit as st

from Daily_TBill_Scraping import get_todays_rf

uri = f"mongodb+srv://{st.secrets['mongo_username']}:{st.secrets['mongo_pw']}@cluster0.xhu6g0i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

tbill_db = client['tbill_data']
indian_tbill_data = tbill_db['indian_tbill_data']

todays_date, todays_yield = get_todays_rf()

indian_tbill_data.insert_one({'Date': todays_date, 'Yield': todays_yield})