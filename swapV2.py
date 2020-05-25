#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:36:19 2019

@author: chingfangli
"""
import pandas as pd
import numpy as np


###this module find out the swap flights in dataframe which is flight data and must has 'FL_DATE','ORIGIN_AIRPORT_ID','DEST_AIRPORT_ID'
###### not include read in code
##### took time to run function

class swapV2:
    def __init__ (self,data):
        self.data = data
    def swapfolder(self):
        frame = self.data
        frame = frame.groupby(['FL_DATE','ORIGIN_AIRPORT_ID','DEST_AIRPORT_ID'])
        frame = frame.apply(lambda x : x.sort_values(['FL_DATE','CRS_DEP_TIME'], ascending = True))
        frame = frame.reset_index(drop = True)
        
        for j in range(0,len(frame)):
           if frame['CRS_DEP_TIME'][j]<100:
               frame['CRS_DEP_TIME'][j]=frame['CRS_DEP_TIME'][j]+2400
           elif frame['CRS_ARR_TIME'][j]<100:
               frame['CRS_ARR_TIME'][j]=frame['CRS_ARR_TIME'][j]+2400
        
        for k in range(0,len(frame)):
           if len(str(frame['CRS_DEP_TIME'][k]))==4:
               if len(str(frame['CRS_ARR_TIME'][k]))==3:
                   frame['CRS_ARR_TIME'][k]=frame['CRS_ARR_TIME'][k]+2400
    
        frame['Y/N']=''
        
        for i in range(1,len(frame)):
           if frame['ORIGIN_AIRPORT_ID'].loc[i-1]==frame['ORIGIN_AIRPORT_ID'].loc[i]:
               if frame['DEST_AIRPORT_ID'].loc[i-1]==frame['DEST_AIRPORT_ID'].loc[i]:
                   if frame['CRS_DEP_TIME'].loc[i-1]<frame['CRS_DEP_TIME'].loc[i]:
                       if frame['CRS_ARR_TIME'].loc[i-1]>frame['CRS_ARR_TIME'].loc[i]:
                           frame['Y/N'].loc[i-1]='Y'
                           frame['Y/N'].loc[i]='N'
               
        frame = frame[(frame['Y/N']=='Y')|(frame['Y/N']=='N')]
    
        return frame
    