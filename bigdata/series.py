# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 01:03:05 2025

@author: Admin
"""

#%% 3-1 시리즈 객체 정보 확인
import pandas as pd
import numpy as np

temp = pd.Series([-0.8, -0.1, 7.7, 13.8, 18.0, 22.4, 25.9, 25.3, 21.0, 14.0, 9.6, -1.4])

temp.index = ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월',] #인덱스에 레이블 부여(레이블 인덱스)

print(temp.iloc[5:8]) #슬라이싱


#%% 인덱싱과 슬라이싱

print(temp.loc["6월" : "9월"])
print("----")
print(temp.loc["6월"])
print("----")
print(temp.iloc[[2,5]])

#%% 조건문을 이용한 슬라이싱

#월평균 15도 이상인 월들의 기온
print(temp.loc[temp>=15])

#월평균 15도 이상 25도미만 기온
print(temp.loc[(temp>=15) & (temp <25)])

#월평균 5도미만이거나 25도 이상인 월들의 기온
print(temp.loc[(temp < 5) | (temp >=25)])

#%% where()메서드를 이용한 조건문
print(temp.where(temp >= 15).dropna())

#%% 3-2 시리즈 객체의 산술연산
print(temp.sum())
print(temp.describe())

#%% 3-3 시리즈 객체 내용 변경

salary = pd.Series([20,15,18,30])
score = pd.Series([75,80,90,60], index = ['kor', 'eng', 'math', 'soc'])

# 값 변경 
score.iloc[0] = 85
score.loc['kor'] = 95
score.loc[['math', 'eng']] = [5, 40]

# 값 추가
score.loc['phy'] = 50
Next_idx = salary.size
salary.loc[Next_idx] = 33

# append()메서드를 이용한 값 추가
New = pd.Series({'mus' : 95})