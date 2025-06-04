import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import folium
import json

from matplotlib import font_manager, rc
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# CSV 로드
df = pd.read_csv(r'C:\Users\Admin\Downloads\부산시_이동지수.csv', encoding='cp949')

# 필요없는 열 제거
df = df.drop(columns=['Unnamed: 65'], errors='ignore')

# 월별 컬럼 추출
month_cols = [col for col in df.columns if '월' in col]

# 분기 생성 함수
def get_quarter(col):
    year, month = col.split('.')
    month = int(month.replace('월', ''))
    if 1 <= month <= 3:
        return f'{year}Q1'
    elif 4 <= month <= 6:
        return f'{year}Q2'
    elif 7 <= month <= 9:
        return f'{year}Q3'
    else:
        return f'{year}Q4'

# 분기별 컬럼 맵핑
quarter_map = {col: get_quarter(col) for col in month_cols}

# 2020~2024년만 사용
selected_quarters = [f'{y}Q{q}' for y in range(2020, 2025) for q in range(1, 5)]
df_quarter = df.copy()
df_quarter = df_quarter.melt(id_vars=['행정구역(시군구)별', '연령별', '항목'], value_vars=month_cols,
                             var_name='월', value_name='이동수')
df_quarter['분기'] = df_quarter['월'].map(quarter_map)
df_quarter = df_quarter[df_quarter['분기'].isin(selected_quarters)]

# 분기별 집계
quarter_summary = df_quarter[df_quarter['행정구역(시군구)별'] == '부산광역시']
quarter_summary = quarter_summary.groupby(['분기', '항목'])['이동수'].sum().unstack()

# 그래프 시각화
quarter_summary.plot(kind='bar', figsize=(15, 6))
plt.title('분기별 부산광역시 인구 이동 추이 (2020~2024)')
plt.ylabel('인원수')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.legend(title='항목')
plt.show()

# -------------------------
# 상관관계 분석
# -------------------------
pivot_df = df[df['행정구역(시군구)별'] == '부산광역시']
pivot_df = pivot_df[pivot_df['항목'].isin(['총전입[명]', '총전출[명]', '순이동[명]'])]

pivot_df = pivot_df.pivot_table(
    index='연령별', columns='항목', values=month_cols, aggfunc='first'
)
pivot_df.columns = ['_'.join(col).strip() for col in pivot_df.columns.values]

pivot_df['총전입합'] = pivot_df[[c for c in pivot_df.columns if '총전입' in c]].astype(float).sum(axis=1)
pivot_df['총전출합'] = pivot_df[[c for c in pivot_df.columns if '총전출' in c]].astype(float).sum(axis=1)
pivot_df['순이동합'] = pivot_df[[c for c in pivot_df.columns if '순이동' in c]].astype(float).sum(axis=1)

print("\n이동 지표 간 상관관계:")
print(pivot_df[['총전입합', '총전출합', '순이동합']].corr())


