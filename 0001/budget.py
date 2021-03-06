#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:59:56 2020

@author: charleskeenan
"""

class Category:
    instances = []
    def __init__(self, name):
        self.name = name
        self.ledger = []
        Category.instances.append(self)
        
    def get_balance(self):
        total_funds = 0
        for item in self.ledger:
            total_funds += item["amount"]
        return total_funds
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": float(amount), "description": description})
        
    def withdraw(self, amount, description=""):
        total_funds = self.get_balance()
        if float(amount) <= total_funds:
            amount = float(amount) * -1
            self.ledger.append({"amount": float(amount), "description": description})
            return True
        else:
            return False
        
    def transfer(self, amount, target):
        total_funds = self.get_balance()
        target_category = target.name
        if float(amount) <= total_funds:
            target.ledger.append({"amount": float(amount), 
                                "description": f"Transfer from {self.name}"})
            amount = float(amount) * -1
            self.ledger.append({"amount": float(amount), 
                                "description": f"Transfer to {target_category}"})
            return True
        else:
            return False
        
    def check_funds(self, amount):
        total_funds = self.get_balance()
        if total_funds >= amount:
            return True
        else:
            return False
        
    def __str__(self):
        s = "*" * ((30 - len(self.name))//2) + str(self.name)
        s = s + "*" * (30 - len(s)) + "\n"
        for item in self.ledger:
            s += item['description'][:23].ljust(23) + "{:.2f}".format(item['amount']).rjust(7)+"\n"
        s += "Total: " + str(self.get_balance())
        return s