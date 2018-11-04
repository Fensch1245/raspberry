import sys
import get_info
import ConfigParser
import os
# from lxml import html
# import requests

# page = requests.get('http://192.168.2.102/ay')
# tree = html.fromstring(page.content)

import urllib2
contents = urllib2.urlopen("http://192.168.2.102/ay").read()
print(contents)
# print(tree.text())


#import requests

#r = requests.get('http://192.168.2.102/ay')
#print(r.text)
 
# import urllib3
# http = urllib3.PoolManager()
# r = http.request('GET', 'http://192.168.2.102/ay')
# r.status
# print(r.status)
# r.data
# print(r.data)