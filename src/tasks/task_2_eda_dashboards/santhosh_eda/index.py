import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit as st
import datetime
import matplotlib.pyplot as plt
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.set_page_config(
  page_icon=
  "https://omdena.com/wp-content/uploads/2023/04/logo_sao_paulo_chapter.png",
  layout="wide",
  page_title="Sao_Paulo",
  initial_sidebar_state="expanded")

with open("styles.css", "r") as source_style:
  st.markdown(f"<style>{source_style.read()}</style>", unsafe_allow_html=True)
  st.header("Monitoring and Predicting Subway Passenger Demand in São Paulo City Using Machine Learning")
  banner_image = Image.open("sao_paulo_banner.png")
  st.image(banner_image, width = 500)

with st.sidebar:
  selected = option_menu(
    menu_title="Main Menu",
    options=[
      "Project Information", "Data Collection", "Interactive Data Analysis",
      "Insights", "Dashboards", "Contributors"
    ],
    default_index=0,
  )

entryByStation = pd.read_csv("alllines_pes_complete.csv")
transportByLine = pd.read_csv("alllines_ptl_complete.csv")
entryByLine = pd.read_csv("publiclines_pel_complete.csv")
entryByStation['date'] = pd.to_datetime(entryByStation['date']).dt.date


if selected == "Project Information":
  st.title("Project Background")
  st.write("São Paulo city is the capital of the Brazilian state with the same name. It is the most populous city in Brazil and the fourth most populous in the world. São Paulo Metropole or the Great São Paulo Area joins 39 cities with around 27 million people and has different urban problems, including public transportation planning.")

  st.title("Problem Statement")
  st.write("The São Paulo city subway system comprises 6 lines with 91 stations. Every day on average more than 4 million people are transported. Although the system is under continuous update with new lines and stations being constructed, the passenger demand is still higher than transportation capacity in critical times every day. Only recently in the last years, the data for passenger demand has been opened to public access. There is no open monitoring system, dashboards, or predictive models to help the people and community decision-makers to understand the evolution and forecast the passenger demand for better urban planning.In this project, the Omdena São Paulo, Brazil Chapter team aims to develop a monitoring and predicting system for subway passenger demand using machine learning. With a duration of 5-weeks, this project aims to: - Data Collection and Preprocessing. - Exploratory Data Analysis - Data Visualization. - Model Development and Training. - Web App Development.")
           
if selected == "Data Collection":
  option = st.selectbox("Explore The Datasets",
                        ("Passenger Entry by Station - All Lines",
                         "Passenger Transported by Line - All Lines",
                         "Passenger Entry by Line - Public Lines"))

  if option == "Passenger Entry by Station - All Lines":
    entryByStation = dataframe_explorer(entryByStation, case=False)
    st.dataframe(entryByStation)
  elif option == "Passenger Transported by Line - All Lines":
    transportByLine = dataframe_explorer(transportByLine, case=False)
    st.dataframe(transportByLine)
  else:
    entryByLine = dataframe_explorer(entryByLine, case=False)
    st.dataframe(entryByLine)
    
if selected == "Interactive Data Analysis":
  today = datetime.date.today()
  tomorrow = today + datetime.timedelta(days=1)
  start_date = st.date_input('Start date',  datetime.date(2021, 1, 1))
  end_date = st.date_input('End date',  datetime.date(2021, 3, 3))
  
  if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date: `%s`' % (start_date, end_date))
  else:
    st.error('Error: End date must fall after start date.')
    
  date = (entryByStation['date'] > start_date) & (entryByStation['date'] <= end_date)
  x = entryByStation["date"].loc[date]
  y = entryByStation.loc[date]
  y = y["line"]
  fig = plt.figure()
  plt.plot(x, y)
  plt.xlabel("Date")
  plt.ylabel("Line")
  st.pyplot(fig)
 
