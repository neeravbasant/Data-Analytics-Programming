# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 09:40:37 2014

@author: Neerav Basant
"""

####################
#    Question 5    #
####################

import urllib

while True:
    
    try:
        url = raw_input("Enter url: ")
        page = urllib.urlopen(url)
        print "Web Address is valid"
        break
    
    except:
        print "Invalid url - Enter a valid one"
        continue
    
fhand = page.read()
print fhand[:3000]

count = 0

for i in fhand:
    count += 1
    
print " The number of characters in the document are %d" % count


####################
#    Question 6    #
####################

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
    
    addressCode = js['results'][0]['address_components']
    
    temp = ""
    for address in addressCode:
        if "country" in address["types"]:
            temp = address["short_name"].encode('ascii','ignore')
        
    if temp == "":
        print "Country Code: None"
    
    else:
        print temp