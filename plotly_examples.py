#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:15:48 2021

@author: sandeep
"""

import numpy as np
import pandas as pd
import plotly as pl
import plotly.io as pio
import plotly.offline as po
import cufflinks as cf

# make it offline for free open source, online require paid account
po.init_notebook_mode(connected=(True))
cf.go_offline()

# plotly will not work in spyder, so assign broswer mode
pio.renderers.default='browser'


df = pd.DataFrame(np.random.rand(100,5,), columns=['A','B','C','D','E'])
df.iplot(kind='scatter', x='A', y='B', mode='markers')

df.scatter_matrix()

df2 = pd.DataFrame({'x':[3,4,7,8,9],'y':[1,2,3,4,5],'z':[6,7,8,4,3]})

# surface example
cf.datagen.sinwave(10,.25).iplot(kind="surface",theme='solar', colorscale='brbg', margin=(0,0,0,0))