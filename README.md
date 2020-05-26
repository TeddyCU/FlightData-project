# FlightData-project
## In this project the main goal is to understand the routes for flights of United states airlines and to search the possible reason for delay
### list of all data set:
#### flight data: specific airline data recording plane activity across a year
#### airport data: recorded the airport information
#### master data:  N-number of Air craft which support plane type 
#### cftref data: aircraft type information
#### airline data: airline information
#### map data: accurate map information
 
## First, this step is used for reading the mega data into Python kernel and creating the module called 'readflightdata.py'
#### Creating class called 'totaldata' which includes flightdata, airportdata, masterdata, acftrefdata, airlinedata, and mapdata and support the data cleanse and exploration.

## Second, this step is trying to understand busiest routes by different time periods
#### Using the module called 'separatedbytime.py' to organizing data and separating the mega data into year periods, month periods, week periods, day periods.

## Third, this step is trying to track routes of each filght and visualize the data for a year
#### Using the module called 'tailtrack.py' to plot the specific tail number of flight and wondering to classify similar plots 

## Forth, this step is making the statistic analysis of aircrafts number in each airline companies
### Using the module called 'countplanebyairline' to find the number of aircrafttype which work as reference for route plots

## Fifth, this step is trying to find out couple aircrafts which has same destination and first craft bound eariler but arrive late than second craft.
#### Using the module called 'swapV2' to plot the time series data and find out the markers which indicates the air craft arrive late compared to its twin craft.



