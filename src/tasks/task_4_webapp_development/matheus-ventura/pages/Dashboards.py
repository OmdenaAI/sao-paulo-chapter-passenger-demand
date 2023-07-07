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
    page_title='Dashboards - Omdena São Paulo Brazil Chapter',
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
    Page for dashboards developed by team members.
    """
)

col1, col2, col3 = st.columns((1, 1 ,1))

with col1:
    with st.container():
        st.write('### [Analysis of demand over the years](https://be4lima-omdena-sao-paulo-chapter-streamlit-dashboard-6da1br.streamlit.app/)')
        st.markdown(
            """
            Analysis of pre and pos COVID demand.

            Developed by Beatriz Lima.
            """)
        st.button('Open link', on_click=open_page, args=('https://be4lima-omdena-sao-paulo-chapter-streamlit-dashboard-6da1br.streamlit.app/',), key=1)
    
    st.markdown('---')

    with st.container():
        st.write('### [Passengers per Station and Shortest Distance](https://anshcs-sau-paulo-metro-demand-eda-streamlitdashboardapp-gwneql.streamlit.app/)')
        st.markdown(
            """
            Plots for passengers entries at each station and shortest route between stations.

            Developed by Ansh CS.
            """)
        st.button('Open link', on_click=open_page, args=('https://anshcs-sau-paulo-metro-demand-eda-streamlitdashboardapp-gwneql.streamlit.app/',), key=2)

    st.markdown('---')

    with st.container():
            st.write('### [Subway Passenger Demand - Tableu](https://public.tableau.com/app/profile/vandriele.barbosa/viz/Subway_passenger_demand/home?publish=yes)')
            st.markdown(
                """
                Plots for Total passenger demand, Business, Saturday, Sunday Means and Daily Max.

                Developed by Vandriele Barbosa.
                """)
            st.button('Open link', on_click=open_page, args=('https://public.tableau.com/app/profile/vandriele.barbosa/viz/Subway_passenger_demand/home?publish=yes',), key=7)

with col2:
    with st.container():
        st.write('### [Passengers transported demand by lines](https://rogerio-chaves-eda-sao-paulo-subway-app-fu49dh.streamlit.app/)')
        st.markdown(
            """
            Analysis of demand on business and weekend days.
            Timeline of infrastructure changes on subway system.

            Developed by Rogerio Chaves.
            """)
        st.button('Open link', on_click=open_page, args=('https://rogerio-chaves-eda-sao-paulo-subway-app-fu49dh.streamlit.app/',), key=3)

    st.write('---')

    with st.container():
        st.write('### [Exploratory Data Analysis - Power BI](https://app.powerbi.com/view?r=eyJrIjoiYjVhNTVlNmYtY2NiNy00NWIzLWI2NzUtMjAxMjI0OGQ5YjAxIiwidCI6ImFiNjViNmQzLWU5ZDEtNDRhOS05OTAzLTEyMTE4NzZlYzY5ZSJ9)')
        st.markdown(
            """
            Analysis of demand by year.

            Developed by Beatriz Lima.
            """)
        st.button('Open link', on_click=open_page, args=('https://app.powerbi.com/view?r=eyJrIjoiYjVhNTVlNmYtY2NiNy00NWIzLWI2NzUtMjAxMjI0OGQ5YjAxIiwidCI6ImFiNjViNmQzLWU5ZDEtNDRhOS05OTAzLTEyMTE4NzZlYzY5ZSJ9',), key=4)

    st.markdown('---')

    with st.container():
            st.write('### [Interactive Data Analysis](https://sp-trainway.streamlit.app/)')
            st.markdown(
                """
                Data visualization and interactive plots.

                Developed by R. Santhosh Kumar.
                """)
            st.button('Open link', on_click=open_page, args=('https://sp-trainway.streamlit.app/',), key=8)



with col3:
    with st.container():
        st.write('### [Interval Between Trains](https://ibt-metro-sp-o0jwk9mpzh.streamlit.app/)')
        st.markdown(
            """
            Analysis of interval between trains for the public lines.

            Developed by Matheus Ventura.
            """)
        st.button('Open link', on_click=open_page, args=('https://ibt-metro-sp-o0jwk9mpzh.streamlit.app/',), key=5)

    st.write('---')

    with st.container():
        st.write('### [Subway Passenger Demand in São Paulo City - Power BI](https://app.powerbi.com/view?r=eyJrIjoiYTRmZGY0NzItYWYxMC00ODY3LThlMDUtNjI5NzJiZWZiMjQ5IiwidCI6IjY1YzgwM2ExLThmYTYtNGVkOC04MTllLWUzODMyMDNkMDBkNSJ9)')
        st.markdown(
            """
            Analysis of passengers transported and passengers entrance.

            Developed by Indrajith C.
            """)
        st.button('Open link', on_click=open_page, args=('https://app.powerbi.com/view?r=eyJrIjoiYTRmZGY0NzItYWYxMC00ODY3LThlMDUtNjI5NzJiZWZiMjQ5IiwidCI6IjY1YzgwM2ExLThmYTYtNGVkOC04MTllLWUzODMyMDNkMDBkNSJ9',), key=6)

