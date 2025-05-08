# -*- coding: utf-8 -*-
"""
Created on Mon May  5 16:07:22 2025

@author: Admin
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd

iris = pd.read_csv(r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\iris.csv")

#%% iris의 sepal_length 값이 20 ~ 90% 사이의 값을 가지는 데이터들만 iris3에 저장

iris3 = iris[(iris['Sepal_Length'] >= iris['Sepal_Length'].quantile(0.2)) & (iris['Sepal_Length'] <= iris['Sepal_Length'].quantile(0.9))]

#%% iris3의 species를 비율을 pie로 나타내어 보기

iris3['Species'].value_counts().plot.pie(ylabel = "", title = "iris3 Species", autopct = "%0.0f%%")

plt.show()

#%% iris3의 모든 변수의 상관 계수를 heatmap 으로 나타내어 보기

iris3 = iris3.drop(['Species'], axis = 1)
iris3_corr = iris3.corr()
sns.heatmap(data = iris3_corr, annot = True, fmt = '.5f')

plt.show()
