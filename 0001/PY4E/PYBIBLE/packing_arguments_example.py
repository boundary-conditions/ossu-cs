#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:39:12 2020

@author: keenan
"""

""" This one takes a list of tuples as an argument"""
def list_maker(*letters):
    final = list()
    for letter in letters:
        final.append(letter)
    return final

"""this takes as many keyword arguments as you want """
def kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))
        


kwargs(Charles = '36', Colleen = '28', Chido = '6', Fern = '3')