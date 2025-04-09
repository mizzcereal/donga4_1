# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:46:31 2025

@author: Admin
"""

#%% 판다스 시리즈 객체 생성

import pandas as pd

age = pd.Series([25,34,19,45,60])
age

type(age)

data = ['Spring', 'Summer', 'Fall', 'Winter']
season = pd.Series(data)

print(season.iloc[2]) # iloc는 절대적인 위치로 이동(인덱스 2의 값)

#%% 판다그 데이터프레임 객체 생성

import pandas as pd

score = pd.DataFrame([[85,96,40,95],
                      [73,69,45,80],
                      [78,50,60,90]])

score

print(score.index)

print(score.iloc[1,2])

#%% 넘파이 배열과 판다스 배열

import pandas as pd
import numpy as np

w_np = np.array([65.4, 71.3, np.nan, 57.7])
weight = pd.Series(w_np)
weight

w_np2 = pd.index.to_numpy(weight)
w_np2

#%% 판다스 Series와 DataFrame의 행과열에 레이블을 부여하는 방법

age.index = ['John', 'Jane', 'Tom', "Luka", "LOL"]
age

print(age.loc['Jane'])
print(age.iloc[1])

score.index = ["john", "jane", "tom"]
score.columns = ['kor', 'eng', 'math', 'science']

print(score.loc['tom', 'math'])
print(score.iloc[2,2])