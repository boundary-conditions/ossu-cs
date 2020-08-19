#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:03:14 2020

@author: keenan
"""


class Produce:
    def __init__(self, fruit=True, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.is_fruit = fruit
        
    def is_veg(self):
        if self.is_fruit:
            s
        
    def __del__(self):
        return "Produce consumed"
    def __str__(self):
        return "Statement"
    
    
    
    


