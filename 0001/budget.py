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
        self.ledger.append({"amount": int(amount), "description": description})
        
    def withdraw(self, amount, description=""):
        total_funds = self.get_balance()
        if int(amount) <= total_funds:
            amount = int(amount) * -1
            self.ledger.append({"amount": int(amount), "description": description})
            return True
        else:
            return False
        
    def transfer(self, amount, target):
        total_funds = self.get_balance()
        target_category = target.name
        if int(amount) <= total_funds:
            target.ledger.append({"amount": int(amount), 
                                "description": f"Transfer from {self.name}"})
            amount = int(amount) * -1
            self.ledger.append({"amount": int(amount), 
                                "description": f"Transfer to {target_category}"})
            return True
        else:
            return False
            
    
    
        