#!/usr/bin/env python
# coding: utf-8

# In[25]:


low_prices  = [100, 200, 400, 800, 1000]    # 리스트에 5일간의 저가(low_prices), 고가 정보(high_prices) 저장
high_prices = [150, 300, 430, 880, 1000]   

volatility = []   # 변동폭을 volatility 리스트로 저장
for i in range(len(low_prices)):   # range(len()) 함수로 원소 갯수 지정
    volatility.append(high_prices[i] - low_prices[i])  # append() 함수로 volatility 리스트에 변동폭 = 고가 정보 - 저가 정보 저장
print(volatility)


# In[ ]:




