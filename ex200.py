#!/usr/bin/env python
# coding: utf-8

# In[28]:


ohlc = [["open", "high", "low", "close"],  # 리스트에 3일 간의 ohlc 데이터 저장
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

profit = 0      # profit 이라는 변수를 지정, 0부터 시작
for row in ohlc[1:]:            # 슬라이싱 메서드 [1:] 을 사용하여 ohlc 리스트의 두 번째 행부터 반복문 실행
    profit += (row[3] - row[0]) # profit 이라는 변수에 각 행마다 종가(row[3]) - 시가(row[0]) 더하기  
print(profit)

