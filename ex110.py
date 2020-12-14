#!/usr/bin/env python
# coding: utf-8

# In[14]:


if True :             # True 라는 조건을 만족하기 때문에 3이 출력되고, 마지막은 조건이 없으므로 5가 그대로 출력된다.
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

