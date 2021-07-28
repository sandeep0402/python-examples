#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 18:19:29 2021

@author: sandeep
"""

import seaborn as sns

print("In built example datasets in seaborn are: ", sns.get_dataset_names())
diamond = sns.load_dataset("diamonds")

dist = sns.distplot(diamond['price'])

rug = sns.rugplot(diamond['x'])

kde = sns.kdeplot(diamond['price'])
