#!/usr/bin/env python
# coding: utf-8

# In[39]:


class OMG:
    def print():       # print() 안에 self가 없으므로 
print("Oh my god")

mystock = OMG()        # OMG class로부터 mystock이라는 객체를 만들고 .를 찍어 메서드를 호출하면 자동으로 mystock 객체가 ()안으로 넘어가기 때문에 에러가 발생한다.
mystock.print()        # OMG.print(mystock)

