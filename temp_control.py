import sys
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

 print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
