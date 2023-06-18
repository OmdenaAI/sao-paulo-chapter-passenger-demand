# Key Insights


## From The Pandas Profiling and Basic EDA


* All the passengers transported data fields (total , daily max , MDU etc) are highly correlated with each other.

* There are some missing values are Line 15 data

* Line 1 and Line 3 servers maximum passengers out of all the lines


## From Plotting the trend PTL data


* All lines are closely corelated except L15. Also L15 has quite less passengers that other lines. I think a probable explanation can be that it is a the latest line built with only 10 out of 18 stations operational right now and is currently under expansion project. Another peculiar detail is that it is the only line under study which is monorail although I am not sure whether that can be a reason or not.

* Before COVID, the data shows semi annual seasonality (especially apparent in the MDU chart) with substantial dip in the middle months of the year (June - July) . A probable reason for that can be vacation periods, and cold weather conditions.

* Such seasonality is not observed during 2020-2021 and 2021-2022 . It is because this was the recovery period against COVID and hence a sort of linear trend is observed with lack of substantial seasonality.

* In 2022-2023, trend can be seen to be getting saturated year by year. Also the semi annual seasonality is appearing to be getting restored with similar "humps" appearing as pre Covid.

* I also verified this seasonality observation using Pacf and Acf plots and they also show a high correlation at 6th month which seems to verify the graphical observation.

## Corelating Sao Paulo Covid cases data with passengers data


* A negative relationship is found out between the passengers travelling and the new covid deaths and cases. For analysis simplicity I took line 2 data for analysis since passengers travelling in all the lines are closely correlated and hence choosing one or aggregating all lines should bring similar results.

* The correlations between passengers travelling and new covid cases came almost -0.4 and new covid deaths came almost -0.3 which is substantial amount of negative correlation.

* Another noteworthy observation is that passengers travelling is positively correlated with accumulated cases and accumulated deaths. A possible reason can be that accumulated cases and deaths are themselves correlated to time and hence as we move forward in time, with covid recovery, passengers travelled increased and also accumulated deaths and cases increased.