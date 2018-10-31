import sys
import Adafruit_DHT
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('config.ini')

print(config.get('DEFAULT', 'set_temp'))

test = 47
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


def temp():
	return temperature

def main():
    print(temp())

if __name__ == "__main__":
    import sys
    main()


