#!/usr/bin/env python
# coding: utf-8

# In[17]:


import requests   # import 메서드로 다른 프로그램으로부터 requests 데이터를 불러옴 
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']  # get() 메서드로 비트코인의 가격 정보를 딕셔너리로 가져옴

# btc 딕셔너리 안에는 시가(opening_price), 종가(closing price), 최고가(max_price), 최저가(min_price) 등이 저장되어 있음

변동폭 = float(btc['max_price']) - float(btc['min_price'])  # 변동폭 = 최고가 - 최저가
시가 = float(btc['opening_price'     # 변동폭, 시가, 최고가라는 변수를 btc 딕셔너리 안의 값을 float 데이터 타입으로 입력받는다.  
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:     # (시가+변동폭)이 최고가보다 높을 경우 "상승장"  
    print("상승장")
else:                          # 그렇지 않은 경우 "하락장" 문자열을 출력한다.
    print("하락장")

