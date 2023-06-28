import streamlit as st

st.set_page_config(
    page_title='Solution',
    layout='wide',
    page_icon='images/omdena_logo.png',
    menu_items={'Get Help': 'https://omdena.com/local-chapters/sao-paulo-brazil-chapter/',
                'Report a bug': 'https://omdena.com/local-chapters/sao-paulo-brazil-chapter/',
                'About': '###### Developed by Omdena São Paulo, Brazil Local Chapter'}
)

st.markdown("""
    <style>
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True
)

st.sidebar.image('images/Omdena-Banner.png')

st.markdown('# Solution')

st.write(
    """
    With a duration of 5-weeks, this project aimed to:
    ## Data Collection and Preprocessing
    The main source for the data about the subway system is available at
    [Portal da Transparência](https://transparencia.metrosp.com.br/search/field_topic/opera%C3%A7%C3%A3o-27).
    The main object was to extract and prepare the data for non-portuguese speakers, and also
    ready for the exploration and modelling.

    ## Exploratory Data Analysis & Data Visualization
    The focus here was to understand the data, answer questions and discover insights
    about the subway system and changes due the COVID-19 pandemic. More info at [Insights](Insights)
    and dashboards developed by the team members at [Dashboards](Dashboards).

    ## Model Development and Training


    ## Web App Development
     
    """
)