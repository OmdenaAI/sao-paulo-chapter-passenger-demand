import streamlit as st 
import pandas as pd 
import folium
import os
from streamlit_folium import st_folium 
import visuals 

pes_df = pd.read_csv(r"C:\OMDENA\Project\sao-paulo-chapter-passenger-demand\src\tasks\task_2_eda_dashboards\data\alllines_pes_complete.csv")
pes_df['date'] = pd.to_datetime(pes_df['date'])

def main():
    st.title("My Streamlit App for EDA ")
    st.subheader("This is a streamlit dash board for showing the various visuals and plots for the Omdena São Paulo Chapter project: 'Monitoring and Predicting Subway Passenger Demand in São Paulo City Using Machine Learning'")
    
def map():
    # Month dropdown
    selected_year = st.selectbox("Select a year", [2021, 2022, 2023])
    selected_month = st.selectbox(
        "Select a month",
        ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]
    )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)

    
    
    selected_line = st.radio("Select an option", ["all", "1", "2", "3", "4", "5", "15"],index=0, format_func=lambda x: x, key="radio")

    st.write("Selected line:", selected_line)

    
    visuals.ShowMap(selected_month,selected_year,selected_line)
    
def Shortdist():
    stations = list(pes_df['station'].unique())
    start_station = st.selectbox('Select start station', stations)
    end_station = st.selectbox('Select end station', stations)

    if start_station == end_station:
        st.warning("Start and end stations cannot be the same. Please choose different stations.")
    else:
        st.success(f"You selected {start_station} as the start station and {end_station} as the end station.")
        # Perform further actions or computations with the selected stations
        visuals.FindShortest_path(start_station.strip(),end_station.strip())
if __name__ == "__main__":
    
    main()
    # Add items to the side menu
    st.sidebar.header("Menu")
    st.sidebar.title("Navigation")
    selected_option = st.sidebar.radio("Select an option", ["Map", "Shortest Distance"])
    if selected_option == "Map":
        map()
    elif selected_option == "Shortest Distance":
        Shortdist()
        
