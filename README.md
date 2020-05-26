# FlightData-project
## In this project the main goal is to understand the routes for flights of United states airlines and to search the possible reason for delay
### list of all data set
#### flight data: specific airline data recording plane activity across a year
#### airport data: recorded the airport information
#### master data:  N-number of Air craft which support plane type 
#### cftref data: aircraft type information
#### airline data: airline information
#### map data: accurate map information
 
## First, to read the mega data into Python, creating the module called 'readflightdata.py'
### Creating class called 'totaldata' which includes flightdata, airportdata, masterdata, acftrefdata, airlinedata, amd mapdata and next support the data cleanse and exploration.

## second, try to understand busiest of routes by diferent time periods
### using the module called 'separatedbytime.py'organizing and separate the data sets into year periods, month periods, week periods, day periods.

## third, make the track of each filght and visualize the routes of a year
### using the module called 'tailtrack.py'plotting the specific tail number of flight and wondering to classify similar route plot 

## forth, make the statistic analysis of planes number in each airline companies
### using the module called 'countplanebyairline'finding the number of aircraft type which make reference for route plots

## fifth, tried to find out couple aircrafts which has same destination and first craft bound eariler but arrive late than second craft.
### using the module called 'swapV2'ploting the time series data and find out the markers which indicates the air craft arrive late compared to its couple craft.



