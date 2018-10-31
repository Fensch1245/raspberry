import sys
import get_info
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('config.ini')

print(config['DEFAULT']['set_temp'])

print get_info.temp()



