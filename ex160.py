#!/usr/bin/env python
# coding: utf-8

# In[20]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py'] # 리스트에 파일 이름 저장
for 변수 in 리스트:
    split = 변수.split(".")                     # 리스트 안의 변수를 split(".") 메서드로 . 을 기준으로 파일 이름을 나눈다
    if (split[1] == "h") or (split[1] == "c"): # 슬라이싱[1]과 논리 연산자 or을 사용해서 확장자가 .h나 .c인 파일을 출력한다. 
        print(변수)

