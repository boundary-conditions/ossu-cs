#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 09:46:22 2020

@author: keenan
"""


import socket
import re

url = input('Enter - ')
full_domain = re.search(r'//([a-z].*)/', url)
domain = full_domain.group()[2:-1]



mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #address family and stream type
mysock.connect((domain, 80)) #accepts a tuple
cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode() #can use .encode() instead of the prefix b
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) == 3000:
        break
    print(data.decode(), end='')
    
mysock.close()






# http://data.pr4e.org/romeo.txt

