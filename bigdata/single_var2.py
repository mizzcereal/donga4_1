# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 22:27:28 2025

@author: Admin
"""

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

ds = [60,62, 64, 65, 68, 69]
ds2 = [60, 62, 64, 65, 68, 69, 120]
weight = pd.Series(ds)
weight_heavy = pd.Series(ds2)

print(weight.mean(), weight_heavy.mean())

print(weight.median(), weight_heavy.median())

print(stats.trim_mean(weight,0.2), stats.trim_mean(weight_heavy, 0.2))

#%%
titanic = pd.read_csv(r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\titanic.csv")

titanic.dropna(axis = 0, subset='age')
titanic['age'].plot.hist(ylabel = 'Frequency')


titanic.query('sex=="male"')['age'].plot.hist(alpha=0.5)

titanic['age'].plot.hist(bins=6)

print(titanic['age'].value_counts(bins=6, sort=False))

plt.show()

#%%

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

ser = pd.Series([1,2,3,3])
ser.plot.hist(title = "극래프예제 - 히스토르갦")

#%%
#학생 12명의 취미조사
hobby = pd.Series(['등산', '낚시', '골프', '수영', '등산', '등산', '낚시', '수영', '등산', '낚시', '수영', '골프'])

#취미별 도수분포표
import matplotlib.pyplot as plt
hv = hobby.value_counts(sort = False)
print(hv)

fig, axes = plt.subplots(nrows =2, ncols=2)

hv.plot.bar(ax=axes[0,0])
hv.plot.pie(autopct = "%1.0f%%", ax=axes[0,1])
