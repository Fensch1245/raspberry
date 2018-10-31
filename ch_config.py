import sys
import ConfigParser

print sys.argv[1] # prints var1
print sys.argv[2] # prints var2
print sys.argv[3] # prints var2

def update_val(sys.argv[1], sys.argv[2], sys.argv[3]):
	config = ConfigParser.ConfigParser()
	config.read('/home/pi/raspberry/config.ini')
	config.set(sys.argv[1], sys.argv[2], sys.argv[3])
	with open("/home/pi/raspberry/config.ini", "w+") as configfile:
		config.write(configfile)
