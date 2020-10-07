#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:34:14 2020

@author: charleskeenan
"""

import shape_calculator

rect = shape_calculator.Rectangle(4,8)

print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_diagonal())
rect.set_width(7)
print(rect.get_perimeter())
rect.set_height(12)
print(rect.get_perimeter())


print(rect.get_picture())
rect.set_height(51)
print(rect.get_picture())
print(rect)