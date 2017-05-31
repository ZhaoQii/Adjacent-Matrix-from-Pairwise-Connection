# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:37:16 2017

@author: Qi Zhao (Homepage: zhaoqii.github.io)
"""
import os
import pandas as pd


os.chdir('F:\高铁子网络')    # set your work path here where the raw data file saved

raw = pd.read_excel('高铁子网络原始数据.xls', header = None) # read raw data file
city = raw[0].append(raw[1]).drop_duplicates()  # get all the cities' str names
city = city.reset_index(drop = True)    # match the str name and sequence number
citynum = len(city)     # totality of city

def set_number(item):  # the function to assign sequence number based on item's str name
    number = city[city == item].index.values
    return(int(number))
    
data = raw.copy()   
data[0] = [set_number(x) for x in data[0]]
data[1] = [set_number(x) for x in data[1]]

adjacent = np.mat(np.zeros([citynum, citynum])).astype(int)  # create adjacent matrix
adjacent[data[0].tolist(), data[1].tolist()]=1
adjacent[data[1].tolist(), data[0].tolist()]=1