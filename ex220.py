#!/usr/bin/env python
# coding: utf-8

# In[31]:


def print_max(a, b, c):   
    if a > b and a > c:   # if문을 사용, a가 b와 c보다 크면 a 출력
        print(a)
    elif b > a and b > c:   # elif문을 사용, b가 a와 c보다 크면 b 출력
        print(b)
    else:
        print(c)      # if나 elif 조건문을 모두 만족하지 않으면 c 출력
        
print_max(18, 1, 2)
print_max(18, 19, 2)
print_max(18, 19, 21)

