#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:30:41 2019

@author: chingfangli
"""

import geoplotlib
import pandas as pd



#####
##### use readflightdata module first to read in flight data 
#### need to know what keys to print out by use getkeys code 
### then use plottrack on ploting 
class routetrack:
    def __init__(self, flightdata, mapdata):
        self.flightdata= flightdata
        self.mapdata = mapdata

    def plottrack(self, tailnum, airlinecode):
        frame = self.flightdata
        frame = frame[['TAIL_NUM','OP_UNIQUE_CARRIER','FL_DATE',
          'ORIGIN_AIRPORT_ID','ORIGIN','CRS_DEP_TIME','DEST_AIRPORT_ID',
          'DEST','CRS_ARR_TIME']]
        frame = frame.sort_values(['FL_DATE','CRS_DEP_TIME'], ascending = True).groupby(['TAIL_NUM','OP_UNIQUE_CARRIER']) 
        alldata = frame.get_group((tailnum, airlinecode)).reset_index().drop(columns=['index'])
        origin = alldata['ORIGIN']
        dest = alldata['DEST']
        mergedata_origin = pd.merge(origin,self.mapdata,left_on=['ORIGIN'],right_on=['name'],how = 'left')
        mergedata_origin = mergedata_origin.rename(columns={'lat':'lat_ori','lon':'lon_ori'})
        mergedata_origin = mergedata_origin
        mergedata_dest = pd.merge(dest,self.mapdata,left_on=['DEST'],right_on=['name'],how='left')
        mergedata_dest = mergedata_dest.rename(columns={'lat':'lat_dest','lon':'lon_dest'})
        mergedata_all = pd.concat([mergedata_origin, mergedata_dest], axis=1)
        geoplotlib.graph(mergedata_all,src_lat='lat_ori',src_lon= 'lon_ori',dest_lat='lat_dest',dest_lon='lon_dest',color='Reds',linewidth=2)
        geoplotlib.savefig(tailnum)
        

    def getkeys(self):
        frame = self.flightdata
        frame = frame[['TAIL_NUM','OP_UNIQUE_CARRIER','FL_DATE',
          'ORIGIN_AIRPORT_ID','ORIGIN','CRS_DEP_TIME','DEST_AIRPORT_ID',
          'DEST','CRS_ARR_TIME']]
        frame = frame.sort_values(['FL_DATE','CRS_DEP_TIME'], ascending = True).groupby(['TAIL_NUM','OP_UNIQUE_CARRIER']) 
        frame = frame.groups.keys()
        frame = pd.DataFrame(list(frame),columns=['tailnum','airline'])
        return frame









