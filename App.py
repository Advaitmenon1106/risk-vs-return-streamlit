import streamlit as st
from CAPM import implement_CAPM
from Portfolio import list_potential_portfolios

st.set_page_config(layout='wide')

# Initialize session state for option
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None

def select_capm():
    st.session_state.selected_option = 'CAPM'

def select_portfolio():
    st.session_state.selected_option = 'Portfolio'

with st.sidebar:
    st.header('Choose a feature', divider='red')
    st.button('CAPM', on_click=select_capm)
    st.button('Portfolio', on_click=select_portfolio)

# Check which option is selected and call the appropriate function
if st.session_state.selected_option == 'CAPM':
    implement_CAPM()
elif st.session_state.selected_option == 'Portfolio':
    list_potential_portfolios()
