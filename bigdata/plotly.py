# -*- coding: utf-8 -*-
"""
Created on Wed May  7 13:06:58 2025

@author: user
"""

import matplotlib.image as mpimg
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt

def radar(df, fills, min_max, title=''):
    fig = go.Figure()
    categories = df.columns.to_list()
    categories.append(categories[0])
    i = 0
    while (i < len(df)):
        scores = df.iloc[i, :].to_list()
        scores.append(scores[0])
        fig.add_trace(go.Scatterpolar(
            r=scores,  # 축의 값
            theta=categories,  # 축의 레이블
            fill=fills[i],  # 다각형 채우기 색
            name=df.index[i]  # 다각형 레이블
        ))
        i += 1
        
        fig.update_layout(
            polar_radialaxis_visible=True,
            polar_radialaxis_range=min_max,  # 축의 값 범위
            showlegend=True,
            margin_t=50,  # 상단 여백
            margin_l=100,  # 좌측 여백
            margin_r=100,  # 우측 여백
            margin_b=25,  # 하단 여백
            width=700,  # 그래프의 폭(pixel)
            height=700,  # 그래프의 높이(pixel)
            title_text=title,  # 그래프 제목
            title_font_size=30,  # 제목 폰트 사이즈
            font_size=20  # 폰트 사이즈
            )
        plot(fig)
        
pre = pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\prestige.csv")

df_new = pre[['education', 'income', 'women',  'prestige']]
df_new.set_index(pre['job'], inplace = True)
df_new.loc['avg'] = df_new.mean()
df_new = (df_new - df_new.min()) / (df_new.max() - df_new.min())

df_new = df_new.query("job == 'avg' or job == 'computer.programers'")

fills = [None, 'toself']
radar(df=df_new,
      fills=fills,
      min_max=[0, 1],
      title='Report'
      )
