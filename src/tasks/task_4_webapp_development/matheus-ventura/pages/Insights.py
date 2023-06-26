import streamlit as st

st.set_page_config(
    page_title='Insights',
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

st.markdown('# Insights')

st.write(
    """
    Page for questions, answers and insights.
    """
)