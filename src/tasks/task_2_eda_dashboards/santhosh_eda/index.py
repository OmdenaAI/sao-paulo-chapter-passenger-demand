import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit as st
import datetime
import matplotlib.pyplot as plt
from streamlit_extras.dataframe_explorer import dataframe_explorer

# Set Streamlit page configuration
st.set_page_config(
  page_icon=
  "https://omdena.com/wp-content/uploads/2023/04/logo_sao_paulo_chapter.png",
  layout="wide",
  page_title="Sao_Paulo",
  initial_sidebar_state="expanded")

# Add custom CSS styles
with open("styles.css", "r") as source_style:
  st.markdown(f"<style>{source_style.read()}</style>", unsafe_allow_html=True)

# Create sidebar menu
with st.sidebar:
  selected = option_menu(
    menu_title="Main Menu",
    options=[
      "Project Information", "Data Collection", "Interactive Data Analysis",
      "Insights", "Dashboards", "Contributors"
    ],
    default_index=0,
  )

# Read the data from CSV
entryByStation = pd.read_csv("alllines_pes_complete.csv")
transportByLine = pd.read_csv("alllines_ptl_complete.csv")
entryByLine = pd.read_csv("publiclines_pel_complete.csv")
entryByStation['date'] = pd.to_datetime(entryByStation['date']).dt.date

if selected == "Project Information":
  # Display project information
  st.header(
    "Monitoring and Predicting Subway Passenger Demand in São Paulo City Using Machine Learning"
  )
  banner_image = Image.open("sao_paulo_banner.png")
  st.image(banner_image, width=500)
  st.title("Project Background")
  st.write(
    "São Paulo city is the capital of the Brazilian state with the same name. It is the most populous city in Brazil and the fourth most populous in the world. São Paulo Metropole or the Great São Paulo Area joins 39 cities with around 27 million people and has different urban problems, including public transportation planning."
  )

  st.title("Problem Statement")
  st.write(
    "The São Paulo city subway system comprises 6 lines with 91 stations. Every day on average more than 4 million people are transported. Although the system is under continuous update with new lines and stations being constructed, the passenger demand is still higher than transportation capacity in critical times every day. Only recently in the last years, the data for passenger demand has been opened to public access. There is no open monitoring system, dashboards, or predictive models to help the people and community decision-makers to understand the evolution and forecast the passenger demand for better urban planning.In this project, the Omdena São Paulo, Brazil Chapter team aims to develop a monitoring and predicting system for subway passenger demand using machine learning. With a duration of 5-weeks, this project aims to: - Data Collection and Preprocessing. - Exploratory Data Analysis - Data Visualization. - Model Development and Training. - Web App Development."
  )

if selected == "Data Collection":
  # Display options to explore datasets
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
  # Set global option for deprecated pyplot usage warning
  st.set_option('deprecation.showPyplotGlobalUse', False)
   # Select dataset for interactive data analysis
  dataset_option = st.selectbox(
    "Select Dataset",
    ("Entry by Station", "Transport by Line", "Entry by Line"))
  if dataset_option == "Entry by Station":

    # Plot 1: Line vs. Date
    st.subheader("Line vs. Date")
    st.line_chart(entryByStation["line"])

    # Plot 2: Station vs. DPEA
    st.subheader("Station vs. DPEA")
    st.bar_chart(entryByStation.set_index("station")["dpea"])

    # Plot 3: DPEA Distribution
    st.subheader("DPEA Distribution")
    plt.hist(entryByStation["dpea"], bins=20)
    st.pyplot()

    # Plot 4: Line vs. Station Count
    st.subheader("Line vs. Station Count")
    station_count = entryByStation["line"].value_counts().sort_index()
    st.bar_chart(station_count)

    # Plot 5: Line vs. Mean DPEA
    st.subheader("Line vs. Mean DPEA")
    mean_dpea = entryByStation.groupby("line")["dpea"].mean()
    st.bar_chart(mean_dpea)
  elif dataset_option == "Transport by Line":
    # Plot 2: Line vs. MDU (Business Days Mean)
    st.subheader("Line vs. MDU (Business Days Mean)")
    st.bar_chart(transportByLine.set_index("line")["MDU (Business Days Mean)"])

    # Plot 3: Line vs. MSD (Saturdays Mean)
    st.subheader("Line vs. MSD (Saturdays Mean)")
    st.bar_chart(transportByLine.set_index("line")["MSD (Saturdays Mean)"])

    # Plot 4: Line vs. MDO (Sundays Mean)
    st.subheader("Line vs. MDO (Sundays Mean)")
    st.bar_chart(transportByLine.set_index("line")["MDO (Sundays Mean)"])

    # Plot 5: Line vs. MAX (Daily Max)
    st.subheader("Line vs. MAX (Daily Max)")
    st.bar_chart(transportByLine.set_index("line")["MAX (Daily Max)"])
  elif dataset_option == "Entry by Line":
    # Plot additional visualizations for entryByLine
    st.subheader("Line Chart: Total by Line")
    fig, ax = plt.subplots()
    ax.plot(entryByLine["date"], entryByLine["total"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Total")
    st.pyplot(fig)

    # Plot 2: Line vs. MDU (Business Days Mean)
    st.subheader("Line vs. MDU (Business Days Mean)")
    st.bar_chart(entryByLine.set_index("line")["business_day_mean"])

    # Plot 3: Line vs. MSD (Saturdays Mean)
    st.subheader("Line vs. MSD (Saturdays Mean)")
    st.bar_chart(entryByLine.set_index("line")["saturday_mean"])

    # Plot 4: Line vs. MDO (Sundays Mean)
    st.subheader("Line vs. MDO (Sundays Mean)")
    st.bar_chart(entryByLine.set_index("line")["sunday_mean"])

    # Plot 5: Line vs. MAX (Daily Max)
    st.subheader("Line vs. MAX (Daily Max)")
    st.bar_chart(entryByLine.set_index("line")["max"])
