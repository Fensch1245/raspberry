import sys
import ConfigParser


def update_val(head, line, new_val):
	config = ConfigParser.ConfigParser()
	config.read('/home/pi/raspberry/config.ini')
	config.set(head, line, new_val)
	with open("/home/pi/raspberry/config.ini", "w+") as configfile:
		config.write(configfile)
