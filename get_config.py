import sys
import ConfigParser

print "wadu"

config = ConfigParser.ConfigParser()
config.read('config.ini')

print(config.get('DEFAULT', 'set_temp'))





