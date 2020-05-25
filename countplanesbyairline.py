#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:00:21 2019

@author: chingfangli
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

#####first step to read in file 


class Byairline:
    def __init__ (self, flightdata, master, acftref, airline):
        self.flightdata = flightdata
        self.master = master
        self.acftref = acftref
        self.airline = airline 
 ##### including read all flight data       
    def flight(self):
        path = self.flightdata
        files=glob.glob(path+"/*.csv")
        all = []
        for file in files:
            df = pd.read_csv(file)
            all.append(df)
        frame = pd.concat(all, axis=0,ignore_index=True)
        frame = frame[['OP_UNIQUE_CARRIER','TAIL_NUM']]
        return frame
###### including read in master and acftref data    
    def allaircraft(self):
        frame1 = pd.read_csv(self.master)
        frame1.columns=frame1.columns.map(str.strip)
        frame1=frame1.applymap(str)
        frame1=frame1.applymap(lambda x : x.strip())
        frame1.iloc[:,0]='N'+ frame1.iloc[:,0]
        
        frame2 = pd.read_csv(self.acftref)
        frame2.columns=frame2.columns.map(str.strip)
        frame2=frame2.applymap(str)
        frame2=frame2.applymap(lambda x : x.strip())
        
        frame3 = pd.merge(frame1,frame2,left_on=['MFR MDL CODE'],right_on=['CODE'])
        frame3 = frame3[['N-NUMBER','MODEL']]
        
        return frame3
 ###including read in airline file   
    def sairline(self):
        frame = pd.read_csv(self.airline)
        frame = frame.rename(index = str, columns={'Description':'airline_name'})
        return frame 
    
    
    ###### second step 
###### use this class to merge three data above and create the now many planes the airline has 
class ALTYPE:
    def __init__ (self, flight, aircraft, airline):
        self.flight = flight
        self.aircraft = aircraft
        self.airline = airline
    
    def MMerge(self):
        frame = pd.merge(self.flight,self.aircraft,left_on=['TAIL_NUM'],right_on=['N-NUMBER'])
        frame = pd.merge(frame,self.airline,left_on=['OP_UNIQUE_CARRIER'],right_on=['Code'])
        frame = frame.drop_duplicates(subset = ['TAIL_NUM','MODEL'],keep = 'first')
        frame = frame.groupby(['airline_name','MODEL']).size().reset_index().rename(columns={0:'count'})
        return frame 
    