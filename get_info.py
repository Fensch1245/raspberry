import sys
import Adafruit_DHT

test = 47
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


def get_temp():
	return temperature

def main(argv):
    print(get_value(*argv[1:]))

if __name__ == "__main__":
    import sys
    main(sys.argv)


