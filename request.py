import sys
import get_info
import ConfigParser
import os
import requests

r = requests.get('http://192.168.2.102/ay')
print(r.text)
 
