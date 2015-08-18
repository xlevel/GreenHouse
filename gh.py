import sensor
from config import Config

config = Config()

print sensor.read(config)
