#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


class Account:     # Account 클래스 생성
    # class variable
    account_count = 0    # 초기 잔고 0으로 설정

    def __init__(self, name, balance):   # 생성자에서 예금주와 초기 잔액 입력받도록 함.
        self.deposit_count = 0
        self.deposit_log = []     # 입금과 출금 리스트 생성
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6자리 형태의 계좌번호 생성
        num1 = random.randint(0, 999)    # random.randint() 메서드를 사용하여 난수 생성
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):    # Account 클래스에 입금을 위한 deposit 메서드 추가
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1:     # 입금은 최소 1원 이상 가능
            self.deposit_log.append(amount)    # 입금 내역을 리스트로 저장
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):   # Account 클래스에 출금을 위한 withdraw 메서드 추가 
        if self.balance > amount:
            self.withdraw_log.append(amount)    # 출금 내역을 리스트로 저장
            self.balance -= amount    # 출금은 계좌의 잔고 이상으로 출금할 수 없음

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):      # 출금액 출력
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):      # 입금액 출력
        for amount in self.deposit_log:
            print(amount)


k = Account("Kim", 1000)   # 1000원 입금
k.deposit(100)    # 100원 예금
k.deposit(200)    # 200원 예금
k.deposit(300)    # 300원 예금
k.deposit_history()   # 입금 내역 출력

k.withdraw(100)   # 100원 출금
k.withdraw(200)   # 200원 출금
k.withdraw_history()   # 출금 내역 출력


# In[ ]:




