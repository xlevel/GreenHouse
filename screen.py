# -*- coding: utf-8 -*-
from oled.device import ssd1306
from oled.render import canvas
from PIL import ImageFont
import time

def Write(dateTime, temp, humidity):
	device = ssd1306(port=1, address=0x3C)

	with canvas(device) as draw:
		font = ImageFont.truetype("FreeSans.ttf", 12)
		draw.text((10,5), "Time: {0}".format(time.strftime('%Y-%m-%d %H:%M:%S', dateTime)), font=font, fill=255)
		draw.text((10,25), "Temp: {0:0.1f}\xb0C".format(temp), font=font, fill=255)
		draw.text((10,45), "Humi: {0:0.1f}%".format(humidity), font=font, fill=255)

