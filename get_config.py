import sys
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('config.ini')
result = config.get('DEFAULT', 'set_temp')

print "wadu"

def set_temp():
	return result

def main(*argv):
    print(set_temp())

if __name__ == "__main__":
    import sys
    main(sys.argv)





