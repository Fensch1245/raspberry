import sys
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('/home/pi/raspberry/config.ini')
result = config.get('DEFAULT', 'activate_heater')

def activate_heater():
	return result

def main(*argv):
    print(activate_heater())

if __name__ == "__main__":
    import sys
    main(sys.argv)





