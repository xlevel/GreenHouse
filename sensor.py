import sys
import Adafruit_DHT
from time import time

def read(config):

	humidity, temperature = Adafruit_DHT.read_retry(config.sensor, config.pin)

	return (time(), humidity, temperature)
