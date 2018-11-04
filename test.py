import sys
import get_info
import ConfigParser
import os
#import requests

#r = requests.get('http://192.168.2.102/ay')
#print(r.text)
 
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://192.168.2.102/ay')
r.status
print(r.status)
r.data
print(r.data)