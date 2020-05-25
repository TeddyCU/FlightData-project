#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:45:53 2019

@author: chingfangli
"""
import pandas as pd
import numpy as np
#this module to get all tail number 
#####first step to read in flight data by using readflightdata module
#####and use this one to organize the tailnumber 


class tailnumber:
    def __init__(self,flightdata):
        self.flightdata = flightdata
        
    def Tail(self):
        frame = self.flightdata
        frame = frame[['TAIL_NUM','OP_UNIQUE_CARRIER','FL_DATE',
          'ORIGIN_AIRPORT_ID','ORIGIN','ORIGIN_CITY_NAME','CRS_DEP_TIME','DEST_AIRPORT_ID',
          'DEST','DEST_CITY_NAME','CRS_ARR_TIME','CRS_ELAPSED_TIME']]
        frame = frame.groupby(['TAIL_NUM','OP_UNIQUE_CARRIER']).apply(lambda x: x.sort_values(['FL_DATE','CRS_DEP_TIME'], ascending = True))
        return frame   
    
    
    
    
