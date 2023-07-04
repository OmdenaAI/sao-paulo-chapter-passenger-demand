import streamlit as st

st.set_page_config(
    page_title='Team',
    layout='wide',
    page_icon='images/omdena_logo.png',
    menu_items={'Get Help': 'https://omdena.com/local-chapters/sao-paulo-brazil-chapter/',
                'Report a bug': 'https://omdena.com/local-chapters/sao-paulo-brazil-chapter/',
                'About': '###### Developed by Omdena São Paulo, Brazil Local Chapter'}
)

st.sidebar.image('images/Omdena-Banner.png')

st.markdown('# Team')

st.write(
    """
    Omdena São Paulo Brazil Chapter
    """
)