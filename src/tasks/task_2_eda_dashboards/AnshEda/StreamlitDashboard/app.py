import streamlit as st 
import pandas as pd 
import folium
import os
from streamlit_folium import st_folium 
import visuals 

def main():
    st.title("My Streamlit App for EDA ")
    st.subheader("This is a streamlit dash board for showing the various visuals and plots for the Omdena São Paulo Chapter project: 'Monitoring and Predicting Subway Passenger Demand in São Paulo City Using Machine Learning'")
    selected_year = st.selectbox("Select a year", [2021, 2022, 2023])

    # Month dropdown
    selected_month = st.selectbox(
        "Select a month",
        ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]
    )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)

    
    
    selected_line = st.radio("Select an option", ["all", "1", "2", "3", "4", "5", "15"],index=0, format_func=lambda x: x, key="radio")

    st.write("Selected line:", selected_line)

    
    visuals.ShowMap(selected_month,selected_year,selected_line)

if __name__ == "__main__":
    main()