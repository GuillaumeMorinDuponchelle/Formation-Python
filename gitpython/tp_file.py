# -*- coding. utf-8 -*-
import json
import csv

with open("geoserver.json","r") as jsonFile:
    indices = json.load(jsonFile)
    for feature in indices ['features']:
        print (feature['id'])
        
    for feature in indices ['features']:
            print (feature['geometry']['coordinates'])

    for feature in indices ['features']:
            #print (feature['properties']['date']
            print (feature['properties']['date']['lib_zone'])

    
    
   