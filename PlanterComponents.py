# import GPIO library
# import uart library
import RPi.GPIO as GPIO
from board import SCL,SDA
import busio
from adafruit_pca9685 import PCA9685
import time

GPIO.setmode(GPIO.BCM)

class Pump():
	def __init__(self,pin):
		self.pin = pin
		GPIO.setup(self.pin,GPIO.OUT)
	def On(self):
		GPIO.output(self.pin,GPIO.HIGH)
	def Off(self):
		GPIO.output(self.pin,GPIO.LOW)

class Led():
	def __init__(self,pin):
		self.pin = pin
		GPIO.setup(self.pin,GPIO.OUT)
	def On(self):
		GPIO.output(self.pin,GPIO.HIGH)
	def Off(self):
		GPIO.output(self.pin,GPIO.LOW)

class Doser():
	def __init__(self,p1_pwm,p2_pwm):
		self.p1_pwm = p1_pwm
		self.p2_pwm = p2_pwm
		self.i2c = busio.I2C(SCL,SDA)
		self.pca = PCA9685(self.i2c)
		self.pca.frequency = 60
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
			self.pca.channels[0].duty_cycle = self.p1_pwm
		print('finished dosing at ' + time.strftime('%H:%M:%S'))
		self.pca.channels[0].duty_cycle = 0
		
def main():
	print ('done')

if __name__ == '__main__':
	main()