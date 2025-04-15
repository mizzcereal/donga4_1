# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 17:35:40 2025

@author: user
"""

#%% Pandas로 파일 읽어오기

import pandas as pd
import numpy as np

mpg = pd.read_excel(r"C:\Users\user\Downloads\dfdata\mpg.xlsx")

#경로에 한글이 있으면 engine = 'openpyxl' 추가
#파일내 데이터에 한글이 있으면 encoding = 'utf-8' 추가
#파일 내 첫 줄에 데이터가 있으면 header = None 추가해서 제거 가능

iris = pd.read_csv(r"C:\Users\user\Downloads\dfdata\iris.csv")

exam = pd.read_csv(r"C:\Users\user\Downloads\dfdata\exam.csv")

#%% DataFrame 객체 정보 확인

iris.info()
iris.shape # (150,5)의 형태 출력
iris.shape[1] # 0이면 행 => 150 출력, 1이면 열 => 5 출력 
iris['Species'].unique() # array(['품종1', '품종2' ...]) 출력

iris.loc[:, ~iris.columns.isin(['Species'])]

