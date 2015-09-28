# -*- coding: utf-8 -*-
from oled.device import ssd1306
from oled.render import canvas
from PIL import ImageFont

def Write(time, temperature, humidity)
	device = ssd1306(port=1, address=0x3C)

	with canvas(device) as draw:
		font = ImageFont.truetype("FreeSans.ttf", 12)
		draw.text((10,5), "Time: 12:21:31", font=font, fill=255)
		draw.text((10,25), "Temp: 19.5\xb0C", font=font, fill=255)
		draw.text((10,45), "Humi: 50.0%", font=font, fill=255)

