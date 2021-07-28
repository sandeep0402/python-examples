#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:40:10 2021

@author: sandeep
"""

import pandas as pd


a = [5,10,15,20,30]
b = [10,20,30,40,50]
c = [11,22,33,44,55]
d = [50,100,150,200,250]

e = pd.DataFrame([a,b,c,d], ['A','B','C','D'],['t1','t2','t3','t4','t5'])
e['t6'] = e['t4'] + e['t5']
f = e.drop('C')
f.drop("t2", axis = 1, inplace=True)
print(f)
print("\U0001f600")
