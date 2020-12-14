#!/usr/bin/env python
# coding: utf-8

# In[21]:


result = 1      # 변수 result에 1저장 -> 1부터 시작 
for i in range(1, 11):  # range 함수로 범위를 1~10으로 지정 -> range(처음 숫자. 마지막 숫자 -> 포함 안됨)
    result *= i      # result = result * i
print(result)

