#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a
Created on Tue Jul 16 22:48:11 2019

@author: chingfangli
"""



#########this module is used to read csv file into pandas
######### 


import pandas as pd
import numpy as np
import glob


class totaldata:
######initial data include >>>flightdatapath, airportiddata, masterdata, acftrefdata, airlinedata,geoairportdata
    def __init__ (self, flightdatapath, airportdata, masterdata, acftrefdata, airlinedata,mapdata):
        self.flightdata = flightdatapath
        self.airportdata = airportdata
        self.masterdata = masterdata
        self.acftrefdata = acftrefdata
        self.airlinedata = airlinedata
        self.mapdata = mapdata
#function read overall data for ready to be separate by time 
    def flight(self):
        path = self.flightdata
        files=glob.glob(path+"/*.csv")
        all = []
        for file in files:
            df = pd.read_csv(file)
            all.append(df)
        frame = pd.concat(all, axis=0,ignore_index=True)
        return frame
    
#function read airport including airportid and name
    def airport(self):
        files = self.airportdata
        frame = pd.read_csv(files)
        frame[['name','country']]=frame['Description'].str.split(',',n=1,expand=True)
        return frame

    
#function read master and aircraft type 
    def aircraft(self):
        frame1 = pd.read_csv(self.masterdata)
        frame1.columns=frame1.columns.map(str.strip)
        frame1=frame1.applymap(str)
        frame1=frame1.applymap(lambda x : x.strip())
        frame1.iloc[:,0]='N'+ frame1.iloc[:,0]
        
        frame2 = pd.read_csv(self.acftrefdata)
        frame2.columns=frame2.columns.map(str.strip)
        frame2=frame2.applymap(str)
        frame2=frame2.applymap(lambda x : x.strip())
        
        all = pd.merge(frame1,frame2,left_on=['MFR MDL CODE'],right_on=['CODE'])
        return all
    
#function read airline            
    def airline(self):
        files = self.airlinedata
        frame = pd.read_csv(files)
        return frame
    
#function read map data    
    def geoairportdata(self):
        data = pd.read_csv(self.mapdata)
        data = data.rename(columns={'AIRPORT':'name','LONGITUDE':'lon', 'LATITUDE':'lat' })
        data = data[['name','lat','lon']]
        data = data.dropna()
        data = data.drop_duplicates(subset=['name'])
        return data