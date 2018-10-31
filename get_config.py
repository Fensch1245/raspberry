import sys
import ConfigParser

print "wadu1"

config = ConfigParser.ConfigParser()
config.read('config.ini')
result = config.get('DEFAULT', 'set_temp')

print "wadu2"

def set_temp():
	return result

def main():
    print(set_temp())

if __name__ == "__main__":
    import sys
    main()

print "wadu3"



