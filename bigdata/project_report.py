import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import folium
import json

from matplotlib import font_manager, rc
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 컴퓨터 폴더
# df = pd.read_csv(r'C:\Users\Admin\Downloads\부산시_이동지수.csv', encoding='cp949')
# 노트북 경로
df = pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\부산시_이동지수.csv", encoding='cp949')

# 필요없는 열 제거
df = df.drop(columns=['Unnamed: 65'], errors='ignore')

# 월별 컬럼 추출
month_cols = [col for col in df.columns if '월' in col]

# 분기 생성 함수
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

# 분기별 컬럼 맵핑
quarter_map = {col: get_quarter(col) for col in month_cols}

# melt하여 월별 -> 행으로
df_quarter = df.copy()
df_quarter = df_quarter.melt(id_vars=['행정구역(시군구)별', '연령별', '항목'], value_vars=month_cols,
                             var_name='월', value_name='이동수')
df_quarter['분기'] = df_quarter['월'].map(quarter_map)

# 필요한 조건 필터링: 부산광역시, 항목은 총전입, 1분기만
df_filtered = df_quarter[
    (df_quarter['행정구역(시군구)별'] == '부산광역시') &
    (df_quarter['항목'] == '총전입[명]') &
    (df_quarter['분기'].str.contains('1분기'))
]

# 연도 추출
df_filtered['연도'] = df_filtered['분기'].str.extract(r'(\d{4})').astype(int)

# 분기별 집계
quarter_summary = df_quarter[df_quarter['행정구역(시군구)별'] == '부산광역시']
quarter_summary = quarter_summary.groupby(['분기', '항목'])['이동수'].sum().unstack()

# 제외할 항목-------
exclude_items = ['순이동[명]', '시도간전입[명]', '시도간전출[명]', '총전입[명]', '총전출[명]']
quarter_summary = quarter_summary.drop(columns=exclude_items, errors='ignore')

# 그래프 시각화
quarter_summary.plot(kind='bar', figsize=(15, 6))
plt.title('분기별 부산광역시 내 인구 이동 추이 (2020~2024)')
plt.ylabel('인원수')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.legend(title='항목')
plt.show()




# -----------------------
# 1분기별 파이차트 (2020~2024, 계 제외)
# -----------------------
# 항목 변경: 총전입 → 시도내이동 - 시군구간 전입[명]
df_filtered = df_quarter[
    (df_quarter['행정구역(시군구)별'] == '부산광역시') &
    (df_quarter['항목'] == '시도내이동-시군구간 전입[명]') &
    (df_quarter['분기'].str.contains('1분기'))
]

df_filtered['연도'] = df_filtered['분기'].str.extract(r'(\d{4})').astype(int)

years = [2020, 2021, 2022, 2023, 2024]
fig, axes = plt.subplots(1, 5, figsize=(20, 5))
fig.suptitle("부산시 연령별 1분기 시도내(시군구간) 전입 인구 구성비 (2020~2024)", fontsize=16)

for i, year in enumerate(years):
    data = df_filtered[df_filtered['연도'] == year]
    group = data.groupby('연령별')['이동수'].sum()
    group = group.drop('계', errors='ignore')  # '계' 제외

    axes[i].pie(group, labels=group.index, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    axes[i].set_title(f'{year}년')

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.show()

