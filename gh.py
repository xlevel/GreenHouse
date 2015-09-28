import sensor
import time
import data
import screen
from config import Config

config = Config()

data.Initialise()

while True:
	reading = sensor.read(config)

	print '{0} {1:0.1f}*C, {2:0.1f}%'.format(time.strftime('%Y-%m-%d %H:%M:%S', reading[0]), reading[1], reading[2])

	data.WriteReading(reading[0], reading[1], reading[2])
	
	screen.Write(reading[0], reading[1], reading[2])

	time.sleep(5)
