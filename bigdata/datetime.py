# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 01:14:19 2025

@author: Admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\timeseries.csv"

ts = pd.read_csv(file_path)


ts['new_Date']= pd.to_datetime(ts['Date'])

print(ts)

ts['year'] = ts['new_Date'].dt.year
ts['Date_yr'] = ts['new_Date'].dt.to_period(freq="M")

ts.drop('Date', axis=1, inplace = True)
ts.set_index('new_Date', inplace = True)
print(ts)

print(ts.loc['2015-07'])

#%%
file_path2 = r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\time_series2.csv"
df = pd.read_csv(file_path2)
print(df)

df['new_date'] = pd.to_datetime(df['date'])
df.drop('date', axis=1, inplace = True)
df.set_index('new_date', inplace =True)

def plot_df(df, x, y, title="", xlabel='Date', ylabel="Value", dpi=100):
    plt.figure(figsize=(16,5), dpi=100)
    plt.plot(x,y,color="r")
    plt.xlabel("date")
    plt.ylabel("value")
    plt.title(title)
    plt.show()
    
plot_df(df, x=df.index, y=df['value'], title="Time")