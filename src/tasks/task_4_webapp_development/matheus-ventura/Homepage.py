import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Homepage - Omdena São Paulo Brazil Chapter',
    layout='wide',
    page_icon='images/omdena_logo.png',
    menu_items={'Get Help': 'https://omdena.com/local-chapters/sao-paulo-brazil-chapter/',
                'Report a bug': 'https://omdena.com/local-chapters/sao-paulo-brazil-chapter/',
                'About': '###### Developed by Omdena São Paulo, Brazil Local Chapter'}
)


st.sidebar.image('images/Omdena-Banner.png')

col1, col2 = st.columns((1, 2))

with col1:
    logo = Image.open('images/logo_sao_paulo_chapter.png')
    st.image(logo)

with col2:
    st.write('# Omdena São Paulo, Brazil Chapter: Monitoring and Predicting Subway Passenger Demand in São Paulo City')

st.markdown(
    """
    The São Paulo city subway system comprises 6 lines with 91 stations.
    Every day on average more than 4 million people are transported. 
    Although the system is under continuous update with new lines and stations 
    being constructed, the passenger demand is still higher than transportation 
    capacity in critical times every day. Only recently in the last years,
    the data for passenger demand has been opened to public access.
    There is no open monitoring system, dashboards, or predictive models
    to help the people and community decision-makers to understand the
    evolution and forecast the passenger demand for better urban planning.

    São Paulo city is the capital of the Brazilian state with the same name.
    It is the most populous city in Brazil and the fourth most populous in the world.
    São Paulo Metropole or the Great São Paulo Area joins 39 cities with around
    27 million people and has different urban problems, including public
    transportation planning.

    ## Project goals
    In this project, the Omdena São Paulo, Brazil Chapter team aims to develop
    a monitoring and predicting system for subway passenger demand using
    machine learning.
    """
)
