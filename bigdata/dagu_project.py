# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 23:21:50 2025

@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# ---------------------------
# 1. 부산시 이동지수 데이터 불러오기 및 전처리
# ---------------------------
df = pd.read_csv(r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\대구시_이동지수.csv", encoding='cp949')
df = df.drop(columns=['Unnamed: 65'], errors='ignore')

# 월별 컬럼 추출
month_cols = [col for col in df.columns if '월' in col]

# 분기 매핑 함수
def get_quarter(col):
    year, month = col.split('.')
    month = int(month.replace('월', ''))
    if 1 <= month <= 3:
        return f'{year} 1분기'
    elif 4 <= month <= 6:
        return f'{year} 2분기'
    elif 7 <= month <= 9:
        return f'{year} 3분기'
    else:
        return f'{year} 4분기'

quarter_map = {col: get_quarter(col) for col in month_cols}

# melt 후 분기 열 추가
df_quarter = df.melt(id_vars=['행정구역(시군구)별', '연령별', '항목'], value_vars=month_cols,
                     var_name='월', value_name='이동수')
df_quarter['분기'] = df_quarter['월'].map(quarter_map)

# 1분기, 부산광역시, 항목: 시도내이동-시군구간 전입
df_filtered = df_quarter[
    (df_quarter['행정구역(시군구)별'] == '대구광역시') &
    (df_quarter['항목'] == '시도내이동-시군구간 전입[명]') &
    (df_quarter['분기'].str.contains('1분기'))
].copy()

df_filtered['연도'] = df_filtered['분기'].str.extract(r'(\d{4})').astype(int)

# ---------------------------
# 2. 10~24세 연령대 비율 계산
# ---------------------------
target_ages = ['10 - 14세', '15 - 19세', '20 - 24세']
df_youth = df_filtered[df_filtered['연령별'].isin(target_ages)]

total_movers = df_filtered[~df_filtered['연령별'].isin(['계'])]['이동수'].sum()
youth_movers = df_youth['이동수'].sum()

youth_ratio = youth_movers / total_movers
print(f"🔹 1분기 시군구간 전입 중 10~24세 비율: {youth_ratio:.4f} ({youth_movers} / {total_movers})")

# ---------------------------
# 3. 전입 사유 데이터 불러오기 및 전처리
# ---------------------------
df_reason = pd.read_csv(r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\대구시_전입사유.csv", encoding='cp949')

# 연도 컬럼만 추출
year_cols = ['2020', '2021', '2022', '2023', '2024']

# long 형식으로 변환
df_reason_long = df_reason.melt(
    id_vars=['행정구역(시도)별', '전입사유별'],
    value_vars=year_cols,
    var_name='연도',
    value_name='전입자수'
)
df_reason_long['연도'] = df_reason_long['연도'].astype(int)

# ---------------------------
# 4. 교육 사유 비율 계산
# ---------------------------
df_reason_edu = df_reason_long[df_reason_long['전입사유별'] == '교육']
latest_year = df_reason_long['연도'].max()
df_latest = df_reason_long[df_reason_long['연도'] == latest_year]

df_latest['전입자수'] = pd.to_numeric(df_latest['전입자수'], errors='coerce')
df_reason_edu['전입자수'] = pd.to_numeric(df_reason_edu['전입자수'], errors='coerce')

# NaN 제거 후 합계 계산
edu_movers = df_reason_edu[df_reason_edu['연도'] == latest_year]['전입자수'].dropna().sum()
total_movers_reason = df_latest['전입자수'].dropna().sum()

edu_ratio = edu_movers / total_movers_reason
print(f"🔹 최근 연도({latest_year}) 교육 사유 전입 비율: {edu_ratio:.4f} ({edu_movers} / {total_movers_reason})")

from scipy.stats import chi2_contingency

# ---------------------------
# 5. 카이제곱 검정 (Chi-squared test of independence)
# ---------------------------

# 2x2 교차표 생성
# 행: 그룹 (연령 / 교육)
# 열: 전입 / 비전입 (성공 / 실패)

# 성공: youth_movers, edu_movers
# 실패: total - 성공
contingency_table = np.array([
    [youth_movers, total_movers - youth_movers],
    [edu_movers, total_movers_reason - edu_movers]
])

# 카이제곱 독립성 검정 수행
chi2, pval, dof, expected = chi2_contingency(contingency_table)

print(f"\n📊 카이제곱 검정 결과:")
print(f" - Chi2 통계량: {chi2:.4f}")
print(f" - P-value: {pval:.29e}")
print(f" - 자유도 (dof): {dof}")
print(f" - 기대빈도표:\n{expected}")

if pval < 0.05:
    print("✅ 귀무가설 기각 → 연령과 교육 사유는 전입과 통계적으로 관련이 있음.")
else:
    print("❌ 귀무가설 채택 → 연령과 교육 사유는 전입과 관련이 있다고 보기 어려움.")

# ---------------------------
# 6. [수정] 항목 3개 포함한 연도별 분기별 이동수 stacked bar 그래프
# ---------------------------
df_bar = df_quarter[
    (df_quarter['행정구역(시군구)별'] == '대구광역시') &
    (df_quarter['항목'].isin([
        '시도내이동-시군구간 전입[명]',
        '시도내이동-시군구간 전출[명]',
        '시도내이동-시군구내[명]'
    ]))
].copy()

df_bar['연도'] = df_bar['분기'].str.extract(r'(\d{4})').astype(int)

# 그룹화 및 재구성
df_grouped_bar = df_bar.groupby(['분기', '항목'])['이동수'].sum().unstack().fillna(0)
df_grouped_bar = df_grouped_bar.sort_index()

# 시각화 (그룹형 막대그래프)
x = np.arange(len(df_grouped_bar))  # 분기 index
width = 0.25  # 막대 너비

fig, ax = plt.subplots(figsize=(14, 7))
ax.bar(x - width, df_grouped_bar['시도내이동-시군구간 전입[명]'], width, label='전입', color='skyblue')
ax.bar(x, df_grouped_bar['시도내이동-시군구간 전출[명]'], width, label='전출', color='orange')
ax.bar(x + width, df_grouped_bar['시도내이동-시군구내[명]'], width, label='시군구내', color='green')

ax.set_xticks(x)
ax.set_xticklabels(df_grouped_bar.index, rotation=45)
ax.set_title('2020~2024 대구광역시 분기별 시도내 이동 항목별 추이')
ax.set_xlabel('분기')
ax.set_ylabel('이동 인구수')
ax.legend()
plt.tight_layout()
plt.show()


# ---------------------------
# 7. [수정] 2020~2024년 1분기 연령별 전입 구성비 pie subplot (5개)
# ---------------------------
fig, axs = plt.subplots(1, 5, figsize=(20, 5))
years = [2020, 2021, 2022, 2023, 2024]

for i, year in enumerate(years):
    df_year = df_filtered[
        (df_filtered['연도'] == year) &
        (df_filtered['연령별'] != '계')
    ]
    df_grouped = df_year.groupby('연령별')['이동수'].sum().reset_index()
    df_grouped['이동수'] = pd.to_numeric(df_grouped['이동수'], errors='coerce')
    
    # 연령 정렬
    df_grouped = df_grouped.set_index('연령별').reindex(age_order).dropna().reset_index()
    
    axs[i].pie(df_grouped['이동수'], labels=df_grouped['연령별'], autopct='%1.1f%%',
               startangle=140, textprops={'fontsize': 7})
    axs[i].set_title(f'{year}년 1분기')

plt.suptitle('2020~2024년 1분기 대구광역시 시군구간 전입 연령별 구성비', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
