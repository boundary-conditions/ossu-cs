#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 07:58:49 2020
Creating classes and objects, udemy projects 9-11


@author: keenan
"""
import random
"""Parent class, or super class created with all the information necessary to
construct an object"""

class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        
        for key, value in kwargs.items():
            setattr(self, key, value) #takes data dict, loops through and applies to instance
        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour
    
    def rust(self):
        self.colour = self.rusty_colour
        
    def clean(self):
        self.colour = self.clean_colour
        
    def flip(self):
        heads_options = [True, False]
        result = random.choice(heads_options)
        self.heads = result
        
    def __del__(self): #destrcutor, self is a convention
        return "Coin Spent"
        
    def __str__(self): #defines what comes out when you print this class
        if self.original_value > 0.25:
            return "${} coin".format(int(self.original_value))
        else:
            return "{}c coin".format(int(self.original_value * 100))

""" Child class created, containing object specific data in a dictionary,
which the parent (super) class iterates over to create a unique object """

class Loonie(Coin): #inherits Coin class
    def __init__(self):
        data = {
            'original_value': 1.00,
            'clean_colour': 'gold',
            'rusty_colour': 'greenish',
            'num_edges': 1,
            'thickness': 1.95,
            'diameter': 26.5,
            'mass': 6.27
            }
        super().__init__(**data)
        
class Toonie(Coin):
    def __init__(self):
        data = {
            'original_value': 2.00,
            'clean_colour': 'silver_gold',
            'rusty_colour': 'greenish',
            'num_edges': 1,
            'thickness': 1.75,
            'diameter': 28,
            'mass': 6.92
            }
        super().__init__(**data)
        
class Quarter(Coin):
    def __init__(self):
        data = {
            'original_value': 0.25,
            'clean_colour': 'silver',
            'rusty_colour': None,
            'num_edges': 1,
            'thickness': 1.58,
            'diameter': 23.88,
            'mass': 4.4
            }
        super().__init__(**data)
        def rust(self): #this is polymorphism
            self.colour = self.clean_colour
        
        def clean(self): #not necessary
            self.colour = self.clean_colour
        
class Dime(Coin):
    def __init__(self):
        data = {
            'original_value': 0.10,
            'clean_colour': 'silver',
            'rusty_colour': 'greenish',
            'num_edges': 1,
            'thickness': 1.22,
            'diameter': 18.03,
            'mass': 1.75
            }
        super().__init__(**data)
        def rust(self): #this is polymorphism
            self.colour = self.clean_colour
        
class Nickel(Coin):
    def __init__(self):
        data = {
            'original_value': 0.05,
            'clean_colour': 'silver',
            'rusty_colour': 'greenish',
            'num_edges': 1,
            'thickness': 1.76,
            'diameter': 21.2,
            'mass': 3.95
            }
        super().__init__(**data)
        def rust(self): #this is polymorphism
            self.colour = self.clean_colour


wallet = [Nickel(), Dime(), Quarter(), Loonie(), Toonie()]

for coin in wallet:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]
    
    string = ("{} - Colour: {}, Value: {}, Diameter: {}, Thickness: {}, Edges: {}, Mass: {}"
              .format(*arguments)) #unpack arguments
    print(string)
    

























