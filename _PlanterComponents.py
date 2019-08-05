# import GPIO library
# import uart library

import time

class Pump():
	def __init__(self,pin):
		self.pin = pin

	def On(self):
		print('Pump on')
	def Off(self):
		print('Pump off')

class Led():
	def __init__(self,pin):
		self.pin = pin
	def On(self):
		print('led on')
	def Off(self):
		print('led off')

class Doser():
	def __init__(self,tx,rx,i2c):
		self.tx = tx
		self.rx = rx
		self.ic2 = i2c
		self.measuredEC = 0
		self.flowrate = 1.0
		self.Read() # auto read upon initialising

	def Read(self):
		# read uart pins
		self.measuredEC = 1.0

	def Dose(self,volume):
		duration = int(volume/self.flowrate)
		print('start dosing at ' + time.strftime('%H:%M:%S'))
		for i in range (0,duration):
			time.sleep(1)
		print('finished dosing at ' + time.strftime('%H:%M:%S'))
		# set pwm frequency