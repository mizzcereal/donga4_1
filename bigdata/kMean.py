#%%
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 데이터 준비
df = pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\iris.csv") 
df = df.drop('Species', axis=1)
df.head()

# 데이터 표준화
scaler = StandardScaler()
result = scaler.fit_transform(df)
df_scaled = pd.DataFrame(result, columns=df.columns)
df_scaled.head()

# 차원축소
pca = PCA(n_components=2)          
transform = pca.fit_transform(df_scaled)                 # 2차원으로 축소 
transform = pd.DataFrame(transform)
transform.head()

# 시각화
transform.plot.scatter(x=0, y=1,                         # 산점도
                       title='PCA plot')
plt.show()

#%%
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 준비
df = pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\iris.csv")  
df = df.drop('Species', axis=1)
df.head()

# 데이터 표준화
scaler = StandardScaler()
result = scaler.fit_transform(df)
df_scaled = pd.DataFrame(result, columns=df.columns)
df_scaled.head()

# 군집화
model = KMeans(n_clusters=3, n_init=10, random_state=123) 
model.fit(df_scaled) 

# 군집화 결과 확인
model.cluster_centers_                  # 군집 중심점 좌표
model.labels_                           # 각행의 군집 번호
model.inertia_                          # 군집 평가 점수

# 차원축소
pca = PCA(n_components=2)          
transform = pca.fit_transform(df_scaled)          # 2차원으로 축소 
transform = pd.DataFrame(transform)
transform['cluster'] = model.labels_              # 군집정보 추가
transform.head()

# 시각화
sns.scatterplot(
    data=transform,
    x = 0,                              # x축 
    y = 1,                              # y축
    hue="cluster",                      # 원의 색 
    palette='Set2',                     # 팔레트 선택
    legend=False                        # 범례표시 여부
)

plt.show()
#%%

ks = range(1,10)                    # 군집의 개수
inertias = pd.Series([])            # 군집화 평가 결과

for k in ks:
    model = KMeans(n_clusters=k,
                   n_init=10, random_state=123)
    model.fit(df_scaled)
    inertias.loc[k] = model.inertia_

plt.figure(figsize=(7, 4))
inertias.plot.line(title = 'Inertias Score',
                   xlabel= 'number of clusters, k',
                   ylabel = 'inertia')
plt.show()

#%%
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

df = pd.DataFrame({
    0 : fish_length,
    1 : fish_weight
})

# 데이터 표준화
scaler = StandardScaler()
result = scaler.fit_transform(df)
df_scaled = pd.DataFrame(result, columns=df.columns)
df_scaled.head()

# 군집화
model = KMeans(n_clusters=2, n_init=10, random_state=123) 
model.fit(df_scaled) 

# 군집화 결과 확인
model.cluster_centers_                  # 군집 중심점 좌표
model.labels_                           # 각행의 군집 번호
model.inertia_                          # 군집 평가 점수
df_scaled['cluster'] = model.labels_

# 시각화
sns.scatterplot(
    data= df_scaled,
    x = 0,                              # x축 
    y = 1,                              # y축
    hue="cluster",                      # 원의 색 
    palette='Set2',                     # 팔레트 선택
    legend=False                        # 범례표시 여부
)

plt.show()

#%%
df_scaled = df_scaled.drop('cluster', axis=1)

ks = range(1,10)                    # 군집의 개수
inertias = pd.Series([])            # 군집화 평가 결과

for k in ks:
    model = KMeans(n_clusters=k,
                   n_init=10, random_state=123)
    model.fit(df_scaled)
    inertias.loc[k] = model.inertia_

plt.figure(figsize=(7, 4))
inertias.plot.line(title = 'Inertias Score',
                   xlabel= 'number of clusters, k',
                   ylabel = 'inertia')
plt.show()