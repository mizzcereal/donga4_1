# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 13:50:53 2025

@author: zmffk
"""

#%%

# 1. 데이터 확인
import pandas as pd

df = pd.read_csv(r"C:\Users\user\Downloads\부산교통공사_월별 역별 권종별 승하차 정보_20231231.csv", encoding='euc-kr')
df2 = pd.read_csv(r"C:\Users\user\Downloads\부산교통공사_년도별_영업손익.csv", encoding='utf-8')

#%%
df = df.groupby('연월')[['무임', '승차']].sum().reset_index()
#%%
df['무임비율'] = df['무임'] / df['승차']
#%%
import pandas as pd

# CSV 파일 불러오기
df4 = pd.read_csv(r"C:\Users\user\Downloads\부산교통공사_월별 역별 권종별 승하차 정보_20231231.csv", encoding='euc-kr')

# 연도와 월 분리
df4['연도'] = df4['연월'].str[:4]
df4['월'] = df4['연월'].str[5:7]

# 연도별-월별 승차 인원 합계 구하기
monthly_boarding = df4.groupby(['연도', '월'])['승차'].sum().reset_index()

# 연도별 총 승차 인원 계산
yearly_total = monthly_boarding.groupby('연도')['승차'].sum().reset_index()
yearly_total.rename(columns={'승차': '연도별총승차'}, inplace=True)

# 연도별 총 승차와 병합
merged = pd.merge(monthly_boarding, yearly_total, on='연도')

# 월별 비율 계산 (%)
merged['월별승차비율(%)'] = (merged['승차'] / merged['연도별총승차']) * 100

merged = merged.astype({'연도': int, '월': int});
#%%

monthly_profit = pd.merge(merged, df2, on='연도')

# 월별 영업손익 계산: 연간 손익 * 월 비율 / 100
monthly_profit['월별 영업손익 (억원)'] = (
    monthly_profit['연간 영업손익 (억원)'] * monthly_profit['월별승차비율(%)'] / 100
)

# 결과 정렬 및 출력
monthly_profit_sorted = monthly_profit.sort_values(['연도', '월'])

# 필요한 열만 보기 좋게 정리
result = monthly_profit_sorted[['연도', '월', '월별승차비율(%)', '월별 영업손익 (억원)']]
result['연월'] = result['연도'].astype(str) + '-' + result['월'].astype(str).str.zfill(2)
result = result.drop(columns=['연도', '월'])

#%%
merged_df = pd.merge(df, result, on='연월', how='inner')
#%%
#그래프에서 이상치가 보인다 2019년도의 코로나 시기와 이상하리 만큼 낮은 적자를 기록 하고 있따
# 그래서 2019년도를 제거하고 상관관계 및 시각화 실시

merged_df = merged_df[~merged_df['연월'].str.contains('2019')]
#%%

merged_df.corr(numeric_only=True, method='pearson')
#merged_df.corr(numeric_only=True, method='spearman')
#merged_df.corr(numeric_only=True, method='kendall')

#%%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.font_manager as fm
import seaborn as sns

# 한글 폰트 설정 (Windows 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  # 음수 깨짐 방지

# 데이터 준비
X = merged_df[['무임비율']]
y = merged_df['월별 영업손익 (억원)']

# 학습/검증용 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 모델 평가
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📉 평균 제곱 오차 (MSE): {mse:.2f}")
print(f"📈 결정 계수 (R² Score): {r2:.2f}")

# 회귀선 시각화
plt.figure(figsize=(10, 6))
sns.regplot(x=X['무임비율'], y=y, line_kws={"color": "red"})
plt.title("무임비율에 따른 월별 영업손익 회귀분석")
plt.xlabel("무임비율")
plt.ylabel("월별 영업손익 (억원)")
plt.grid(True)
plt.show()
#%%
# 실제 vs 예측 비교 그래프
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('실제 월별 영업손익 (억원)')
plt.ylabel('예측 월별 영업손익 (억원)')
plt.title('실제값 vs 예측값')
plt.grid(True)
plt.show()

#%%
