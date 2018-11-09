import sys
import get_info
import ConfigParser
import os
import webbrowser
# from lxml import html
# import requests

# page = requests.get('http://192.168.2.102/ay')
# tree = html.fromstring(page.content)


# print(tree.text())


#import requests

#r = requests.get('http://192.168.2.102/cm?cmnd=Power')
#print(r.text)
 
import urllib3
http = urllib3.PoolManager()

webbrowser.open('http://192.168.2.123/cm?cmnd=Power%20toggle')

#http.request('GET', 'http://192.168.2.123/cm?cmnd=Power%20toggle')

state = http.request('GET', 'http://192.168.2.123/cm?cmnd=Power')

if 'OFF' in state.data:
	status = 0
else:
	status = 1
	
print status