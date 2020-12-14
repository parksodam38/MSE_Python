#!/usr/bin/env python
# coding: utf-8

# In[2]:


종목 = []        # 종목 생성

class Stock:    # Stock 클래스 생성
    def __init__(self, name, code, per, pbr, 배당수익률):   # 생성자에서 종목명, 종목 코드, PER, PBR, 배당수익률을 입력받을 수 있도록 함.
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):      # get_name, get_code : 종목명과 종목 코드를 리턴하는 메서드
        return self.name

    def get_code(self):
        return self.code

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)    # 종목 리스트에 append 함수를 이용하여 삼성, 현대차, LG전자 추가
종목.append(현대차)
종목.append(LG전자)

for i in 종목:    # 종목 리스트 안의 객체들 불러오기
    print(i.code, i.per)  # i -> Stock 클래스의 객체를 바인딩하기 때문에 .을 찍으면 클래스 안의 객체에 접근 가능

