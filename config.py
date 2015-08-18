import Adafruit_DHT


class Config:
	def __init__(self):
		self.sensor = Adafruit_DHT.AM2302
		self.pin = 4
