# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 23:36:43 2025

@author: Admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mpg = pd.read_excel(r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\mpg.xlsx")

mpg.plot.scatter(x="cty", y="displ")
plt.show()

print(mpg.info())

vars = ['cty', 'displ', 'hwy']
pd.plotting.scatter_matrix(mpg[vars])
plt.show()

#%% 다중산점도 그룹색상
iris = pd.read_csv(r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\iris.csv")

dict = {"setosa" : "red", "versicolor": "green", "virginica":"blue"}
colors = list(dict[key] for key in iris.Species)

print(colors)

iris.plot.scatter(x = "Petal_Length", y= "Petal_Width", s = 50, c = colors, marker = "*")

#%% 다중산점도 범례

fig, ax = plt.subplots()

for label, data in iris.groupby('Species'):
    ax.scatter(x=data['Petal_Length'], y=data["Petal_Width"], s =30, c = dict[label], marker = 'o', label=label)
    print(data)
    
ax.set_xlabel("Petal_Length")
ax.set_ylabel("Petal_Width")
ax.legend()
plt.show()

#%% 상관계수 분석

beers = [5,2,9,8,3,7,3,5,3,5]
bal = [0.1, 0.03, 0.19, 0.12, 0.04, 0.0095, 0.07, 0.06, 0.02, 0.05]

dict = {"beers": beers, "bal":bal}
df = pd.DataFrame(dict)
print(df)

df.plot.scatter(x = "beers", y="bal", title = "Beers")

#선형적관계출력
w, b = np.polyfit(beers, bal, 1)
plt.plot(beers, w*np.array(beers)+b)

plt.show()

#상관계수 계산
print(df['beers'].corr(df['bal']))