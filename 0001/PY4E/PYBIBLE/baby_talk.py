#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:10:32 2020

@author: keenan
"""
import random
#from random import choice

questions = ["Mommy, why does everybody have a bum?: ", 
             "Mommy, who's my daddy?: ", 
             "Mommy, where did fluffy go to live?: ",
             "Mommy, whats two plus two?: ",
             "Mommy, where do babies come from?: "]

question = random.choice(questions)

answer = input(question).strip().lower()
exit_answer = 'just because'

while answer != exit_answer :
    answer = input("Why?: ").strip().lower()
    
print("Oh, okay")