import sensor
import time
from config import Config

config = Config()

while True:
	reading = sensor.read(config)

	print '{0} {1:0.1f}*C, {2:0.1f}%'.format(time.strftime('%Y-%m-%d %H:%M:%S', reading[0]), reading[1], reading[2])

	time.sleep(5)
