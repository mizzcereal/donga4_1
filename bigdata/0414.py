# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:39:49 2025

@author: user
"""

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

result = []

def hollys_store(result):
    for page in range(1,10):
        holly_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' %page
        html = urllib.request.urlopen(holly_url)
        soupHollys = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupHollys.find('tbody')
        for store in tag_tbody.find_all('tr'):
            if len(store) <= 3:
                break
            store_td = store.find_all('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            result.append([store_name] + [store_sido] + [store_address] + [store_phone])
            
    return

hollys_store(result)


columnname = ['name', 'sido', 'address', 'phone']
df = pd.DataFrame(result, columns = columnname)


sidoinfo = ['서울', '부산', '대구', '울산', '인천', '광주', '세종'] #가져올리스트

s = []
for i in range(len(df)):
    sd = df.iloc[i,1]
    sd=sd[:2]
    s.append(sd)
df['sido'] = s 

df2 = df.query('sido in @sidoinfo')