#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 08:50:22 2020

@author: keenan
"""
time_dictionary = dict()

file = input("Please enter a filename: ").strip()
if len(file) < 1:
    file = 'mbox-short.txt'
fhand = open(file)

for line in fhand :
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
       time = words[5].split(':')
       time_dictionary[time[0]] = time_dictionary.get(time[0], 0) + 1
       
time_list = list(sorted(time_dictionary.items()))

for k, v in time_list :
    print(k, ":", v)

