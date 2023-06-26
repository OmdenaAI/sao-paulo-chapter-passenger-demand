import streamlit as st
from streamlit.components.v1 import html


def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)


st.set_page_config(
    page_title='Dashboards',
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

st.markdown('# Dashboards')

st.write(
    """
    Page for dashboards from all volunteers.
    """
)

col1, col2, col3 = st.columns((1, 1 ,1))

with col1:
    with st.container():
        st.write('### Analysis of demand over the years')
        st.markdown(
            """
            Analysis of pre and pos COVID demand.

            Developed by Beatriz Lima.
            """)
        st.button('Open link', on_click=open_page, args=('https://be4lima-omdena-sao-paulo-chapter-streamlit-dashboard-6da1br.streamlit.app/',), key=1)
    
    st.markdown('---')

    with st.container():
        st.write('### Passengers per Station and Shortest Distance')
        st.markdown(
            """
            Plots for passengers entries at each station and shortest route between stations.

            Developed by Ansh CS.
            """)
        st.button('Open link', on_click=open_page, args=('https://anshcs-sau-paulo-metro-demand-eda-streamlitdashboardapp-gwneql.streamlit.app/',), key=2)

with col2:
    with st.container():
        st.write('### Passengers transported demand by lines')
        st.markdown(
            """
            Analysis of demand on business and weekend days.
            Timeline of infrastructure changes on subway system.

            Developed by Rogerio Chaves.
            """)
        st.button('Open link', on_click=open_page, args=('https://rogerio-chaves-eda-sao-paulo-subway-app-fu49dh.streamlit.app/',), key=3)

    st.write('---')

    with st.container():
        st.write('### Exploratory Data Analysis - Power BI')
        st.markdown(
            """
            Analysis of demand by year.

            Developed by Beatriz Lima.
            """)
        st.button('Open link', on_click=open_page, args=('https://app.powerbi.com/view?r=eyJrIjoiYjVhNTVlNmYtY2NiNy00NWIzLWI2NzUtMjAxMjI0OGQ5YjAxIiwidCI6ImFiNjViNmQzLWU5ZDEtNDRhOS05OTAzLTEyMTE4NzZlYzY5ZSJ9',), key=4)

