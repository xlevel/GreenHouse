import sys
import Adafruit_DHT
from time import gmtime

def read(config):

	humidity, temperature = Adafruit_DHT.read_retry(config.sensor, config.pin)

	return (gmtime(), humidity, temperature)
