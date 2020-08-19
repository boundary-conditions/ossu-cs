#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 22:38:34 2020

@author: keenan
"""

adr_dict = dict()

file= input("Enter a filename: ").strip()
if len(file) < 1 :
        file = 'mbox-short.txt'
fhand = open(file)
for line in fhand :
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    else:
        print(words)
        adr_dict[words[1]] = adr_dict.get(words[1], 0) + 1

new_list = sorted([(v, k) for k, v in adr_dict.items()],reverse=True)

total, name = new_list[0]

print("The most emails came from {} with {} commits".format(name, total))
print(new_list[0])
