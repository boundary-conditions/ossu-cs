#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 09:13:37 2020

@author: keenan
"""
import string
letters = dict()

file = input("Please enter a filename: ").strip()
fhand = open(file)
for line in fhand :
    clean_line = line.translate(line.maketrans('','',string.punctuation))
    clean_line = clean_line.lower().strip()
    for letter in clean_line :
        if letter == " ":
            continue
        elif letter in '1234567890':
            continue
        else:
            letters[letter] = letters.get(letter, 0) + 1


sorted_letters = sorted([(v, k) for k, v in letters.items()], reverse=True)
for k, v in sorted_letters :
    print("There are {} instances of {}".format(k, v))

#print(letters)
#print(clean_line)
