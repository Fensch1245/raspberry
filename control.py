import sys
import get_info
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('config.ini')

print(config['set']['temp'])

print get_info.temp()



