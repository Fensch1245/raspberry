import sys
import ConfigParser


def update_val(sys.argv[1], sys.argv[2], sys.argv[3]):
	config = ConfigParser.ConfigParser()
	config.read('/home/pi/raspberry/config.ini')
	config.set(sys.argv[1], sys.argv[2], sys.argv[3])
	with open("/home/pi/raspberry/config.ini", "w+") as configfile:
		config.write(configfile)
