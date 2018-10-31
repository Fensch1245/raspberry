import sys
import ConfigParser

print "wadu"

config = ConfigParser.ConfigParser()
config.read('config.ini')
result = config.get('DEFAULT', 'set_temp')

print(type(result))

def set_temp():
	return result

def main():
    print(set_temp())

if __name__ == "__main__":
    import sys
    main()




