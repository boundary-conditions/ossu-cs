#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:39:10 2020

@author: keenan
"""
#import string

vowels = ('a','e','i','o','u')

user_string = input("What would you like translated?: ").lower().strip()
word_list = user_string.split()
translated_list = list()
#translated = ""

for word in word_list :
    if word.startswith(vowels):
        word = word + 'yay'
        print(word)
    elif word.startswith(vowels, 1, 2):
        word = word[1:] + word[:1] + "ay"
        print(word)
    else:
        word = word[2:] + word[:2] + "ay"
        print(word)
    translated_list.append(word)
    
translated = " ".join(translated_list).capitalize()
    
# for word in translated_list :
#     if len(translated) < 1:
#         translated = word.capitalize()
#     else:
#         translated = translated + " " + word

#print(user_string)
#print(translated_list)
print(translated)

# try to make punctuation work
#if word.endswith((string.punctuation)):
   # print("works")