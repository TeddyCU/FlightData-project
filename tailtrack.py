#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:26 2019

@author: chingfangli
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

####this module plot a line to track whether the DEST ad ARR are different
##### how to get key by using the getkey function inside the routeplot module


class findtrack:
    def __init__(self, flightdata):
        self.flightdata = flightdata
        
    def getunit(self, tail, airlinecode):
        track = self.flightdata
        track = track[['TAIL_NUM','OP_UNIQUE_CARRIER','FL_DATE','CRS_DEP_TIME',
          'ORIGIN','ORIGIN_CITY_NAME','DEST','DEST_CITY_NAME']]
        track = track.sort_values(['FL_DATE','CRS_DEP_TIME'], ascending = True).groupby(['TAIL_NUM','OP_UNIQUE_CARRIER'])
        track = track.get_group((tail, airlinecode)).reset_index().drop(columns=['index'])
        trackorigin = track[['FL_DATE','ORIGIN']]
        trackdest = track[['FL_DATE','DEST']]
        S1 = track['ORIGIN']
        S2 = track['DEST']
        S3 = pd.concat([S1, S2]).drop_duplicates()
        airporttemp = pd.DataFrame(data = S3, columns = ['place']).reset_index().drop(columns =['index'] )
        airporttemp['tempcode'] = airporttemp.index
        trackorigin=pd.merge(trackorigin,airporttemp,left_on=['ORIGIN'],right_on=['place'],how = 'left')
        trackdest = pd.merge(trackdest,airporttemp,left_on=['DEST'],right_on=['place'],how = 'left')
        series1 = pd.DataFrame(data = trackorigin['tempcode'].values, index= trackorigin['FL_DATE']).rename(columns={0:'origin'})
        series2 = pd.DataFrame(data = trackdest['tempcode'].values, index= trackdest['FL_DATE']).rename(columns={0:'dest'})
        S4 = pd.concat([series1,series2 ], axis=1).reset_index()
        S4['marker']=''
        for i in range(1,len(S4)):
            if S4['origin'].loc[i]!=S4['dest'].loc[i-1]:
                S4['marker'].loc[i-1] = 1
    
        markers = S4.index[S4['marker']==1].tolist()
        plot=S4.plot(x = 'FL_DATE',style='.-',markevery=markers,figsize=(150,5),marker='o',markerfacecolor = 'red')
        fig = plot.get_figure()
        fig.savefig(tail)







