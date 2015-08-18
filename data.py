import sys
import time
import sqlite3

def Initialise():
	try:
		connection = sqlite3.connect('readings.db')

		cursor = connection.cursor()

		cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Readings'")

		if cursor.fetchone() == None:
			print 'No Readings table found. Creating the table now.'

			cursor.execute("CREATE TABLE Readings(Date TEXT, Temp REAL, Humidity REAL)")
			connection.commit()

	finally:
		if connection:
			connection.close()

def WriteReading(dateTime, temp, humidity):
	strTime = time.strftime("%Y-%m-%d %H-%M-%S", dateTime)

	try:	
		connection = sqlite3.connect('readings.db')

		cursor = connection.cursor()
		cursor.execute("INSERT INTO Readings(Date, Temp, Humidity) VALUES ('{0}', {1}, {2})".format(strTime, temp, humidity))
		connection.commit()

	finally:
		if connection:
			connection.close()
