#%%

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\crimeRatesByState2005.csv")

sns.set_theme(rc={'figure.figsize':(7,7)})

sns.scatterplot(
    data =df,
    x="murder",y =  "burglary",
    size="population", sizes=(20,4000),
    hue="state", alpha = 0.5,
    legend = False)

for i in range(0,df.shape[0]):
    if df.murder[i] <=12 :
        plt.text(x=df.murder[i],y=df.burglary[i],s=df.state[i],
                 horizontalalignment='center',size="small",color='dimgray')
plt.xlim(0,12)

plt.show()

#%% 문제 직종별 education과 income에 대해 버블차트 작성
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(rc={'figure.figsize':(7,7)})

pre = pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\prestige.csv")

sns.scatterplot(data = pre, x="education", y= "income",
                size = "women", sizes = (20,4000),
                hue = "type", legend = True)

for i in range(0, pre.shape[0]):
    plt.text(x=pre.education[i], y = pre.income[i], s = pre.job[i],
             horizontalalignment = "center", size = "small", color = "dimgray")

plt.show()

#%%
from plotly.offline import plot
import plotly.express as px
fig =px.line_polar(r=[1,5,2,3,2],theta=['a','b','c','d','e'],
                   line_close=True)


plot(fig)
#%%
# 실습전 라이브러리 설치
# pip install plotly
# pip install kaleido==0.1.0post1


import matplotlib.image as mpimg
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
#####################################################################

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
"""
    # 그래프 저장 & display
    plt.axis('off')
    fig.write_image('rader.png')
    plt.imshow(mpimg.imread('rader.png'))
    plt.show()
 """
#####################################################################

# 데이터 입력
df = pd.DataFrame({
    'Kor': [72, 70, 90, 60, 66],
    'Eng': [84, 85, 95, 70, 85],
    'Math': [71, 40, 88, 80, 75],
    'Sci': [83, 80, 91, 90, 70],
    'Phy': [60, 60, 60, 70, 50]
})
df.index = ['AVG', 'John', 'Tom', 'Smith', 'Grace']
df
fills = [None, 'toself']
radar(df=df.iloc[[0, 3], :],
      fills=fills,
      min_max=[0, 100],
      title='Scores of Smith'
      )

#%%

fills = ['toself', 'toself', 'toself', 'toself']
radar(df=df.iloc[1:, :],
      fills=fills,
      min_max=[0, 100],
      title='Scores of Student'
      )
#%%

