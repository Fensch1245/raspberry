import sys
import ConfigParser




config = ConfigParser.ConfigParser()
config.read('config.ini')


config.set('DEFAULT', 'set_temp', '25')
config.write()

