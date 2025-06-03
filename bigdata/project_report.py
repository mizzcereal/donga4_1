# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 01:16:28 2025
@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv("C:/Users/Admin/Downloads/부산광역시_시군구_각세별_이동자수_20250604011350.csv", encoding='cp949')

# '부산광역시' 전체, 연령별 데이터만 추출 ('계' 제외)
age_df = df[(df['행정구역별'] == '부산광역시') & (df['각세별'] != '계')]

# 필요한 컬럼만 선택
age_df = age_df[['각세별', '2020', '2021', '2022', '2023', '2024']].copy()
age_df.set_index('각세별', inplace=True)
age_df = age_df.astype(int)

# 연도별로 막대그래프 그리기
years = ['2020', '2021', '2022', '2023', '2024']
plt.figure(figsize=(14, 8))

for i, year in enumerate(years):
    plt.bar(
        [x + i*0.15 for x in range(len(age_df.index))],  # 막대 위치를 연도별로 살짝 옆으로 이동
        age_df[year],
        width=0.15,
        label=year
    )

# x축 레이블 설정
plt.xticks([x + 0.3 for x in range(len(age_df.index))], age_df.index, rotation=45)
plt.title('연령대별 연도별 전입자 수 추이 (부산광역시)', fontsize=16)
plt.xlabel('연령대')
plt.ylabel('전입자 수')
plt.legend(title='연도')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

