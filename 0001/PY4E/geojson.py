#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:19:47 2020

@author: keenan
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 'AIzaSyBApATfALzX7gkHfDufJh0wOuKSz_Lhsqc'

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    address = input('Enter location: ') #get map address input from user
    if len(address) < 1: break #if they enter nothing, byebye
    parms = dict() #empty dictionary for parameters
    parms['address'] = address #create  key called address and set its value to the users input
    if api_key is not False: parms['key'] = api_key #false checkin isnt necessary, set key called address with a value of the api key
    url = serviceurl + urllib.parse.urlencode(parms) # concatenate the encoded url with the address and key with the original url
    
    print('Retrieving', url) #print the whole url
    uh = urllib.request.urlopen(url, context=ctx) #send a url encoded with the dictionary parameters and get all the data at this url, and ignore the ssl stuff according to the ctx variable
    data = uh.read().decode() #read and decode the data, then store it in this variable
    print('Retrieved', len(data), 'characters') #print out that you received data of a certain length
    
    try:
        js = json.loads(data) #load the string in the data variable into json so we can look at it
    except:
        js = None #if that fails...
        
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Reatrieve ===')
        print(data) #error checking
        continue
    
    print(json.dumps(js, indent=4)) #print out some data
    
    # lat = js['results'][0]['geometry']['location']['lat'] #set a variable equal to the lat and long lcation of address
    # lng = js['results'][0]['geometry']['location']['lng']
    
    # print('lat', lat, 'lng', lng)
    # location = js['results'][0]['formatted_address'] #print it
    # print(location)
    try:
        addr_comp = js['results'][0]['address_components']
    except:
        print("Error, no address components")
    
    
    for component in addr_comp:
        for k, v in component.items():
            if type(v) is list and v[0] == 'country':
                code = component['short_name']
                print(f"The country code is {code}")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    