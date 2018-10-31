import sys
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('config.ini')
result = config.get('DEFAULT', 'set_temp')



def set_temp():
	return result

def main():
    print(set_temp())

if __name__ == "__main__":
    import sys
    main(sys.argv)





