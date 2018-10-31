import sys
import ConfigParser

config = ConfigParser.ConfigParser()

cfgfile = open("config.ini",'w')

config.set('DEFAULT', 'set_temp', '25')
config.write(cfgfile)

