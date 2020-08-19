#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 08:39:50 2020

@author: keenan
"""

import xml.etree.ElementTree as ET

input = '''
<stuff>
<users>
<user x="2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id>009</id>
<name>Brent</name>
</user>
</users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #like this
print('User count:', len(lst))

lst2 = stuff.findall('user') #need to include parent level elements
print('User count:', len(lst2))