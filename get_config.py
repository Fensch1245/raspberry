import sys
import ConfigParser
import os  
os.environ['PYTHON_EGG_CACHE'] = '/tmp' # a writable directory 

config = ConfigParser.ConfigParser()
config.read('config.ini')
print "wadu"
result = config.get('DEFAULT', 'set_temp')
print "wadu2"


def set_temp():
	return result

def main(*argv):
    print(set_temp())

if __name__ == "__main__":
    import sys
    main(sys.argv)





