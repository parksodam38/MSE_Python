#!/usr/bin/env python
# coding: utf-8

# In[3]:


class 부모:    # 부모 클래스 생성
    def __init__(self):
        print("부모생성")

class 자식(부모):    # 자식(부모) 클래스 생성 -> 부모 클래스 메서드 호출
    def __init__(self):
        print("자식생성")
        super().__init__()   # super() 메서드를 사용하여 자식 클래스에서 부모 클래스의 내용을 사용함.

나 = 자식()

