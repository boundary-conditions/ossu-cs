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
rect.set_width(8)
print(rect.get_perimeter())
rect.set_height(12)
print(rect.get_perimeter())


print(rect.get_picture())
rect.set_height(12)
print(rect.get_picture())
print(rect)

sq = shape_calculator.Square(5)
print(sq.get_area())
print(sq.get_perimeter())
print(sq.get_diagonal())
sq.set_width(7)
print(sq)
print(sq.get_area())
sq.set_height(9)
print(sq)
print(sq.get_perimeter())
sq.set_side(4)
print(sq)
print(sq.get_diagonal())

print(rect.get_amount_inside(sq))

rect.set_height(4)
rect.set_width(4)
print(rect.get_amount_inside(sq))

rect.set_height(1)
rect.set_width(8)
print(rect.get_amount_inside(sq))