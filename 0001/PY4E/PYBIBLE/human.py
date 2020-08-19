#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:52:14 2020

@author: keenan
"""


class Human:
    def __init__(self, name, sex, **kwargs):
        self.name = name
        self.sex = sex
        
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)