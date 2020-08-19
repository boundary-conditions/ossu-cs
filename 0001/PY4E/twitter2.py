#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 08:35:53 2020

@author: keenan
"""

import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

ctx = ssl.create_default_context() #ignore ssl certs (just put it here)
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account: ') #get user input for twitter acct
    if (len(acct) <1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, #ammends 
                         'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    
    js = json.loads(data)
    print(json.dumps(js, indent = 2))
    
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    
    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   *No Status')
            continue
        s = u['status']['text']
        print('   ', s[:50])