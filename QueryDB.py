from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st
import datetime as dt

def Query_DB(date):
    starting_date = dt.datetime.strptime(date, '%d-%m-%Y')
    uri = f"mongodb+srv://{st.secrets['mongo_username']}:{st.secrets['mongo_pw']}@cluster0.xhu6g0i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
    except Exception as e:
        st.write(e)
    
    tbill_db = client['tbill_data']
    indian_tbill_data = tbill_db['indian_tbill_data']
    query = {"Date":{"$gte":starting_date}}

    res = indian_tbill_data.find(query)
    yields = []

    for doc in res:
        yields.append(doc['Yield'])

    return yields
