# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

file = input("Please enter a filename: ").strip()
if len(file) < 1:
    file = 'mbox-short.txt'
fhand = open(file)

for line in fhand :
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        y = re.findall('^From .*@([^ ]*)', line)
        print(y)
        
        
# file = input("Please enter a filename: ").strip()
# if len(file) < 1:
#     file = 'mbox-short.txt'
# fhand = open(file)

# for line in fhand :
#     y = re.findall('^From .*@([^ ]*)', line)
#     print(y)