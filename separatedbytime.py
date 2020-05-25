#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 00:19:50 2019

@author: chingfangli
"""
import pandas as pd
import numpy as np

#####this module is used to find out top counts or busiest of routes by time range 
class separatebytime():
####this is not read file into panda 
####need exist dataframe ahead
    def __init__(self, dataset, airportdata):
        self.dataset = dataset
        self.airportid = airportdata
    
    def byYear(self):
        data = self.dataset.groupby(['ORIGIN_AIRPORT_ID','DEST_AIRPORT_ID']).size().reset_index().rename(columns={0:'count'}).sort_values(by=['count'],ascending=False)
        data = data.loc[data['count'].idxmax()]
        data = pd.Series(data).unique()
        newdata = pd.DataFrame(data = data).transpose().reset_index()
        Var1 = newdata.iloc[:,1]    
        Var2=newdata.iloc[:,2]
        newdata = pd.concat([Var1,Var2],ignore_index=True).unique()
        result = self.airportid.loc[self.airportid['Code'].isin(newdata)==True]
        return result
    
    def byMonth(self,month):        
        data = self.dataset.groupby(['MONTH','ORIGIN_AIRPORT_ID','DEST_AIRPORT_ID']).size().reset_index().rename(columns={0:'count'}).sort_values(by=['count'],ascending=False)   
        data = data.loc[data['MONTH'] == month]
        data = data.loc[data['count'].idxmax()]
        data = pd.Series(data).unique()
        newdata = pd.DataFrame(data = data).transpose().reset_index()
        Var1 = newdata.iloc[:,2]    
        Var2=newdata.iloc[:,3]
        newdata = pd.concat([Var1,Var2],ignore_index=True).unique()
        result = self.airportid.loc[self.airportid['Code'].isin(newdata)==True]
        return result
    
    def byDayofWeek(self,day):        
        data = self.dataset.groupby(['DAY_OF_WEEK','ORIGIN_AIRPORT_ID','DEST_AIRPORT_ID']).size().reset_index().rename(columns={0:'count'}).sort_values(by=['count'],ascending=False)   
        data = data.loc[data['DAY_OF_WEEK'] == day]
        data = data.loc[data['count'].idxmax()]
        data = pd.Series(data).unique()
        newdata = pd.DataFrame(data = data).transpose().reset_index()
        Var1 = newdata.iloc[:,2]    
        Var2=newdata.iloc[:,3]
        newdata = pd.concat([Var1,Var2],ignore_index=True).unique()
        result = self.airportid.loc[self.airportid['Code'].isin(newdata)==True]
        return result
    
    def byDay(self):
        data = self.dataset.groupby(['FL_DATE','ORIGIN_AIRPORT_ID','DEST_AIRPORT_ID']).size().reset_index().rename(columns={0:'count'}).sort_values(by=['count'],ascending=False)
        data = data.loc[data['count'].idxmax()]
        data = pd.Series(data).unique()
        newdata = pd.DataFrame(data = data).transpose().reset_index()
        Var1 = newdata.iloc[:,2]    
        Var2=newdata.iloc[:,3]
        newdata = pd.concat([Var1,Var2],ignore_index=True).unique()
        result = self.airportid.loc[self.airportid['Code'].isin(newdata)==True]
        return result
        