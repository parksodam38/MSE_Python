#!/usr/bin/env python
# coding: utf-8

# In[13]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09'] # date 라는 변수에 key 저장
close_price = [10500, 10300, 10100, 10800, 11000]    # close_price 라는 변수에 values 저장
close_table = dict(zip(date, close_price))           # close_table이라는 변수에 zip() 메서드로 date : close_price 를 묶고, dict 메서드로 저장
print(close_table)

