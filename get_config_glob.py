import sys
import ConfigParser

eintrag = sys.argv[1]

config = ConfigParser.ConfigParser()
config.read('/home/pi/raspberry/config.ini')
result = config.get('DEFAULT', eintrag)

def activate_heater():
	return result

def main(*argv):
    print(activate_heater())

if __name__ == "__main__":
    import sys
    main(sys.argv)





