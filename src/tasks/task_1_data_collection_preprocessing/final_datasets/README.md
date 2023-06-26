# This folder contains the final datasets that should be used by the other teams

There are three datasets available to be used for EDA and modelling team, with the following features/schema:

# Features - Schema

## Passenger entrance by line datasets ("pel_complete.csv")

- date - Month when the data was collected - datetime (yyyy-mm-dd)
- line - Subway line number - int
- total - Total of passengers that entered the station on that month - int
- business_day_mean - (MDU) Mean of passengers that entered the station on that month on business day - int
- saturday_mean - (MSA) Mean of passengers that entered the station on that month on saturdays - int
- sunday_mean - (MD0) Mean of passengers that entered the station on that month on sundays - int
- max - (MAX) Maximum of passengers entered on one day on that month - int

## Daily average passenger entrance by station on business days datasets ("pes_complete.csv")

- date - Month when the data was collected - datetime (yyyy-mm-dd)
- line - Subway line number - int
- station - Subway station - categorical?
- dpea - Daily average passenger entrance by station - int

## Passengers transported by line datasets ("ptl_complete.csv)

- date - Month when the data was collected - datetime (yyyy-mm-dd)
- line - Subway line number - int
- total - Total of passengers transported by line on that month - int
- business_day_mean - (MDU) Mean of passengers transported on that month on business day - int
- saturday_mean - (MSA) Mean of passengers transported on that month on saturdays - int
- sunday_mean - (MD0) Mean of passengers transported on that month on sundays - int
- max - (MAX) Maximum of passengers transported on one day on that month - int