# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 17:35:40 2025

@author: user
"""

#%% Pandas로 파일 읽어오기

import pandas as pd
import numpy as np

# mpg = pd.read_excel(r"C:\Users\user\Downloads\dfdata\mpg.xlsx")
mpg = pd.read_excel(r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\mpg.xlsx")

#경로에 한글이 있으면 engine = 'openpyxl' 추가
#파일내 데이터에 한글이 있으면 encoding = 'utf-8' 추가
#파일 내 첫 줄에 데이터가 있으면 header = None 추가해서 제거 가능

# iris = pd.read_csv(r"C:\Users\user\Downloads\dfdata\iris.csv")
iris = pd.read_csv(r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\iris.csv")

# exam = pd.read_csv(r"C:\Users\user\Downloads\dfdata\exam.csv")
exam = pd.read_csv(r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\exam.csv")

#%% DataFrame 객체 정보 확인

iris.info()

iris.shape # (150,5)의 형태 출력
iris.shape[1] # 0이면 행 => 150 출력, 1이면 열 => 5 출력 
iris['Species'].unique() # array(['품종1', '품종2' ...]) 출력

iris.loc[:, ~iris.columns.isin(['Species'])]

#%% dataframe 기술통계

print(exam.index)
print(exam.columns)

print(exam.describe())

print("---math----")
print(exam[['math','english']])
print(exam['math'].mean())

#%% dataframe 정렬

print(exam.sort_values(by = 'math')) # sort_values(by = "기준열")메서드 사용 
print(exam.sort_values(by = 'math', ascending = False)) #sort_values(by = "기준열")안에 ascending = False를 넣으면 내림차순

#%% 조건에 따른 변수 만들기
exam['total'] = exam['math'] + exam['science']
exam['test'] = np.where(exam['total'] >= 160, "합격", "탈락")

print(np.where(exam['test'] == "합격"))

#%% 조건에 맞는 행 추출하기

print(exam.query('nclass == 2'))

#1반이면서 수학점수가 50점 이상
print(exam.query('nclass == 1 & math >=50'))

#1,3,5반 추출
print(exam.query('nclass in [1, 3, 5]'))

#%% 상위 10%추출하기
print(exam.quantile(0.9))

#%% 열 삽입하기

#중간에 열 삽입하는 방법 => df.insert(loc, name, array)
exam.insert(5, 'phy', [n for n in range(0, 20)])

#%% 자료형 확인 후 자료형 변환
print(exam.dtypes) # df.dtypes로 자료형 확인
exam['test_str'] = exam['test'].astype(str)

print(exam.dtypes)

#%% 행 열 삭제

exam = exam.drop(['test'], axis = 1) # axis = 1은 열
print(exam)

exam = exam.drop([3], axis = 0) # axis = 0은 
print(exam)

#%% 행/열 합계

#df.sum()메서드 사용

