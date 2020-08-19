#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 07:58:49 2020
Creating classes and objects, udemy projects 9-11


@author: keenan
"""


class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, insufficient funds")
    
    def statement(self):
        print("Account balance: ${}".format(self.balance))
        
        
class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)
        
    def __str__(self):
        return "{} account balance is ${}".format(self.name, self.balance)


class Saving(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)
    def __str__(self):
        return "{} saving account balance is ${}".format(self.name, self.balance)
        
charles = Current("Charles", 500)

charles.deposit(100)