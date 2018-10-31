import sys
import get_info
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

print(config['set']['temp'])

print get_info.temp()



