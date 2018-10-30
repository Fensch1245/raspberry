import sys
import Adafruit_DHT
require_once "/home/pi/raspberry/web/index.php"

sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

print temperature

