#!/usr/bin/env python
# coding: utf-8

# In[33]:


def 함수0(num):
    return num * 2   # 7. num = 14 * 2 = 28

def 함수1(num):    # 5. num = 12 로 시작
    return 함수0(num + 2)   # 6. return 명령어 -> 함수0 호출 , num = 12 + 2 = 14

def 함수2(num):    # 2. 변수 c가 함수2(2)를 지정하므로 num = 2
    num = num + 10    # 3. num = 2 + 10 = 12 로 변경
    return 함수1(num)   # 4. return 명령어 -> 함수1 호출

c = 함수2(2)   # 1. 변수 c가 함수2 를 지정하므로 함수2 부터 시작
print(c)       # 제일 마지막으로 return된 28 출력

