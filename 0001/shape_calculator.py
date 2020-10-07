#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 08:44:38 2020

@author: charleskeenan
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, new_width):
        self.width = new_width
        
    
    def set_height(self, new_height):
        self.height = new_height
    
    
    def get_area(self):
        area = self.width * self.height
        return area
        
    
    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter
    
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.width ** 2) ** .5
        return diagonal
        
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        else:
            picture_string = "*" * self.width + "\n"
            picture_string = picture_string * self.height
            return picture_string 
    
    def get_amount_inside(self, other_shape):
        horizontal = self.width // other_shape.width
        vertical = self.height // other_shape.height
        total = horizontal * vertical
        return total
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side
        
    def set_width(self, new_width):
        self.width, self.height = new_width, new_width
        
    
    def set_height(self, new_height):
        self.height, self.width = new_height, new_height
        
    def __str__(self):
        return f"Square(side={self.width})"


