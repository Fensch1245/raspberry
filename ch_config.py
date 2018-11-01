#     python  ch_config.py section option newvalue

import sys
import ConfigParser

def main():
	section = sys.argv[1]
	option = sys.argv[2]
	value = sys.argv[3]
	
	config = ConfigParser.ConfigParser()
	config.read('/home/pi/raspberry/config.ini')
	config.set(section, option, value)
	with open("/home/pi/raspberry/config.ini", "w+") as configfile:
		config.write(configfile)

main()