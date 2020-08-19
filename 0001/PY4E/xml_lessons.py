#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 08:32:14 2020

@author: keenan
"""

import xml.etree.ElementTree as ET

data = '''<person>
<name>Chuck</name>
<phone type="intl">
+1 902 399 8868
</phone>
<email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))