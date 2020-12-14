#!/usr/bin/env python
# coding: utf-8

# In[29]:


def message1():   # def 메서드로 message1 함수 지정
    print("A")    
    
def message2():   # def 메서드로 message2 함수 지정
    print("B")
    
def message3():   # def 메서드로 message3 함수 지정
    for i in range (3) :   # range 함수를 이용하여 message2 3번 반복
        message2()      
        print("C")         # message2 함수는 B를 출력하므로 , B, C를 반복해서 출력
    message1()             # 마지막으로 message1의 A 1개 출력
    
message3()  

