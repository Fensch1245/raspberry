import sys
import get_info
import ConfigParser
import os
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

http.request('GET', 'http://192.168.2.123/cm?cmnd=Power%20toggle')


print status

	#http://192.168.2.102/cm?cmnd=status
	
	#http://192.168.2.102/cm?cmnd=Power
	
	#https://github.com/arendst/Sonoff-Tasmota/wiki/Commands#logging