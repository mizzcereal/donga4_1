# -*- coding: utf-8 -*-
"""
Created on Mon May 12 01:56:36 2025

@author: ekoh2
"""

import json
geo = json.load(open(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\SIG.geojson",encoding='UTF-8'))
#%%

import pandas as pd
df_pop=pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\Population_SIG.csv")
df_pop.info()

#%%
df_pop['code']=df_pop['code'].astype(str)
df_pop.info()

#%%
import folium
import webbrowser
#지도를 생성
m=folium.Map(location=[35.95,127.7],             
           zoom_start=8,
           tiles='cartodbpositron')
file_path='map.html'
m.save(file_path)

# 기본 웹브라우저로 파일 열기

webbrowser.open(file_path)
#%%

folium.Choropleth(
    geo_data=geo,
    data=df_pop,
    columns=('code','pop'),
    key_on='feature.properties.SIG_CD') \
        .add_to(m)


# 지도를 HTML 로 저장
file_path='map.html'
m.save(file_path)

# 기본 웹브라우저로 파일 열기
webbrowser.open(file_path)

#%%계급 구간 정하기
bins=list(df_pop['pop'].quantile([0,0.2,0.4,0.6,0.8,1]))

m=folium.Map(location=[35.95,127.7],             
           zoom_start=8,
           tiles='cartodbpositron')
       
folium.Choropleth(
    geo_data=geo,
    data=df_pop,
    columns=('code','pop'),
    key_on='feature.properties.SIG_CD',
    fill_color='YlGnBu',
    fill_opacity=0.5,
    line_opacity=0.5,
    bins=bins).add_to(m)
# 지도를 HTML 로 저장
file_path='map.html'
m.save(file_path)

# 기본 웹브라우저로 파일 열기
webbrowser.open(file_path)
#%%
#%%서울시 동별 외국인 인구 단계 구분도 만들기
import json
geo_seoul=json.load(open(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\EMD_Seoul.geojson",encoding='UTF-8'))

foreigner = pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\Foreigner_EMD_Seoul.csv")

foreigner['code']=foreigner['code'].astype(str)

bins=list(foreigner['pop'].quantile([0,0.2,0.4,0.5,0.6,0.7,0.8,0.9,1]))

map_seoul =folium.Map(location=[37.56,127],             
           zoom_start=12,
           tiles='cartodbpositron')
folium.Choropleth(
    geo_data=geo_seoul,
    data=foreigner,
    columns=('code','pop'),
    key_on='feature.properties.ADM_DR_CD',
    fill_color='Blues',
    nan_fill_color='White', # 결측치 색상
    fill_opacity=0.5,
    line_opacity=0.5,
    bins=bins).add_to(map_seoul)

file_path='map.html'
map_seoul.save(file_path)

# 기본 웹브라우저로 파일 열기
webbrowser.open(file_path)
#%%

import pandas as pd
df_pop=pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\Population_SIG.csv")
df_pop.info()

df_pop['code']=df_pop['code'].astype(str)
pcode_df=df_pop.query('code.str.startswith("26")')

import pandas as pd
import folium

pusan_pop=pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\pusan_pop(1).csv",encoding='euc-kr')

pcode_df.drop(['pop'],axis=1,inplace=True)

pusan_pop['총인구']=pusan_pop['총인구'].astype(int)
pcode=pd.merge(pcode_df, pusan_pop,how='inner',on='region')

pusan_pop.info()
#%%
geo_busan=json.load(open(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\SIG.geojson",encoding='UTF-8'))
feature=[x for x in geo_busan['features'] if x['properties']['SIG_CD'].startswith('26')]
geo_busan['features']=feature



#%%
bins=list(pcode['총인구'].quantile([0,0.2,0.4,0.5,0.6,0.7,0.8,0.9,1]))

map_pusan =folium.Map(location=[35.17,129.07],             
           zoom_start=12,
           tiles='cartodbpositron')
folium.Choropleth(
    geo_data=geo_busan,
    data=pcode,
    columns=('code', '총인구'), key_on='feature.properties.SIG_CD',
    fill_color='YlGnBu',
    nan_fill_color='White', # 결측치 색상
    fill_opacity=0.3,
    line_opacity=0.5,
    bins=bins).add_to(map_pusan)

file_path='map.html'
map_pusan.save(file_path)
webbrowser.open(file_path)