import streamlit as st
from CAPM import implement_CAPM

st.set_page_config(layout='wide')

options = {'CAPM': implement_CAPM}

with st.sidebar:
    st.header('Choose a feature', divider='red')
    option_CAPM = st.button('CAPM')

if option_CAPM:
    implement_CAPM()