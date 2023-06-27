import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.sidebar.image('images/Omdena-Banner.png')

st.markdown('# Insights')


def run():
    st.set_option('deprecation.showPyplotGlobalUse', False)

    df = pd.read_csv('data/alllines_ptl_complete.csv', parse_dates=[0], index_col=0, date_format='%Y-%m-%d')
    l1 = df[df['line'] == 1]
    l2 = df[df['line'] == 2]
    l15 = df[df['line'] == 15]
    l3 = df[df['line'] == 3]
    l4 = df[df['line'] == 4]
    l5 = df[df['line'] == 5]

    l1 = l1.asfreq(pd.infer_freq(l1.index))
    l2 = l2.asfreq(pd.infer_freq(l2.index))
    l3 = l3.asfreq(pd.infer_freq(l3.index))
    l15 = l15.asfreq(pd.infer_freq(l15.index))
    l4 = l4.asfreq(pd.infer_freq(l4.index))
    l5 = l5.asfreq(pd.infer_freq(l5.index))

    plt.figure(figsize=(12, 6))
    L1, = plt.plot(l1['MDU (Business Days Mean)'], color='green')
    L2, = plt.plot(l2['MDU (Business Days Mean)'], color='red')
    L3, = plt.plot(l3['MDU (Business Days Mean)'], color='yellow')
    L15, = plt.plot(l15['MDU (Business Days Mean)'], color='blue')
    L4, = plt.plot(l4['MDU (Business Days Mean)'], color='violet')
    L5, = plt.plot(l5['MDU (Business Days Mean)'], color='black')
    for year in range(2018, 2024):
        plt.axvline(datetime(year, 1, 1), color='k', alpha=0.2)

    plt.legend(['Line 1', 'Line 2', 'Line 3', 'Line 15', 'Line 4', 'Line 5'], fontsize=12)

    plt.xlabel("Date")
    plt.ylabel("Business Day Mean of passengers travelled by Line")

    st.pyplot()

    st.write("""

       ## Key Insights
       
       * All lines are closely correlated except L15. Additionally L15 has quite less passengers that other lines. A 
       probable explanation can be that it is a the latest line built with only 10 out of 18 stations operational 
       right now and is currently under expansion project. Another peculiar detail is that it is the only line under 
       study which is monorail although it is not sure whether that can be a reason. 
       
       * Before COVID, the data shows semi annual seasonality (especially apparent in the Mean Business Day 
       Passengers transported chart) with substantial dip in the middle months of the year (June - July) . A probable 
       reason for that can be vacation periods, and cold weather conditions. This seasonality observation was also 
       verified using Pacf and Acf plots and they also show a high correlation at 6th month which seems to verify the 
       graphical observation. 
        
       *  Such seasonality is not observed during 2020-2021 and 2021-2022 . It is because this was the recovery 
       period against COVID and hence a sort of linear trend is observed with lack of substantial seasonality. In 
       2022-2023, trend can be seen to be getting saturated year by year. Also the semi annual seasonality is 
       appearing to be getting restored with similar "humps" appearing as pre Covid. 
   
        * A negative relationship is found out between the passengers travelling and the new covid deaths and cases. 
        For analysis simplicity Line-2 data for analysis since passengers travelling in all the lines are 
        closely correlated and hence choosing one or aggregating all lines should bring similar results. 
        
        * After going through some data of the nominal Gross Domestic Product (GDP) of Brazil month-wise (source: 
        https://fred.stlouisfed.org/series/BRALORSGPNOSTSAM ) and tried to find the relation between the GDP trends 
        of Brazil and the PTL (Passengers Transported) of Sao Paulo and found out high correlation between them .If we 
        compare PTL with the GDP of 1 month prior, the correlation between GDP and PTL reaches 0.8 .Hence using 1 
        month past GDP can be a very good indicator of the upcoming month's PTL trends. 
    

      """)

    return None
