#!/usr/bin/env python
# coding: utf-8

# In[16]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}  # fruit 이라는 변수에 key로 계절, values에 과일 저장
user = input("좋아하는 과일은?")           # input 메서드로 user에게 좋아하는 과일은? 질문을 하도록함
if user in fruit.values():     # if 변수를 사용하여 사용자가 입력한 값이 딕셔너리 값(values)에 포함되어 있으면 정답입니다를 
    print("정답입니다.")    
else:                          # 아닐 경우 오답입니다를 출력하도록 한다.
    print("오답입니다.")

