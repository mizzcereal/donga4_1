# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 12:20:01 2025

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\iris.csv")

iris_2d=df[['Petal_Length']].values

inertia = []
for k in range(2,7):
    km = KMeans(n_clusters = k, random_state = 42)
    km.fit(iris_2d)
    inertia.append(km.inertia_)
plt.plot(range(2,7),inertia)
plt.show()