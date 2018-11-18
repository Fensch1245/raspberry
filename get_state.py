import sys
import ConfigParser
import os

import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://192.168.2.123/cm?cmnd=Power')


if 'OFF' in r.data:
	status = 0
else:
	status = 1

print status

	#http://192.168.2.102/cm?cmnd=status
	
	#http://192.168.2.102/cm?cmnd=Power
	
	#https://github.com/arendst/Sonoff-Tasmota/wiki/Commands#logging