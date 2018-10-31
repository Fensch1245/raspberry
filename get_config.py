import sys
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('config.ini')

print(config.get('DEFAULT', 'set_temp'))





