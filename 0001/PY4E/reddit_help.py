#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:07:07 2020

@author: keenan
"""


# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end='')

# mysock.close()

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    
#     while True:
#         data = mysock.recv(512)
#         if len(data) < 1:
#             break
#         print(data.decode(), end='')

# mysock.close()

    cl = None
    while cl is None or cl > 0:
        data = mysock.recv(512).decode()
        if cl is None:
            headers, data = data.split('\r\n\r\n')
            print(headers)
            for line in headers.splitlines():
                if line.lower().startswith('content-length'):
                    cl = int(line.split()[-1])
                    break
        cl -= len(data)
        print(data, end='')
        
    
        
