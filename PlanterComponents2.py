# import uart library
import RPi.GPIO as GPIO
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
	def __init__(self,p1,p2,p1DutyCycle,p2DutyCycle):
		self.p1 = p1
		self.p2 = p2
		self.p1DutyCycle = p1DutyCycle
		self.p2DutyCycle = p2DutyCycle
		self.measuredEC = 0
		self.flowrate = 1.0
		self.Read() # auto read upon initialising

		GPIO.setup(self.p1,GPIO.OUT)
		GPIO.setup(self.p2,GPIO.OUT)
		self.pump1 = GPIO.PWM(p1,60)
		self.pump2 = GPIO.PWM(p2,60)

	def Read(self):
		# read uart pins
		self.measuredEC = 1.0

	def Dose(self,volume):
		duration = int(volume/self.flowrate)
		print('start dosing at ' + time.strftime('%H:%M:%S'))
		for i in range (0,duration):
			time.sleep(1)
			self.pump1.start(self.p1DutyCycle)
			self.pump2.start(self.p2DutyCycle)
		print('finished dosing at ' + time.strftime('%H:%M:%S'))
		self.pump1.stop()
		self.pump2.stop()
		
		
def main():
	GPIO.cleanup()
	doser = Doser(22,23,50,50)
	doser.Dose(3)
	print ('done')

if __name__ == '__main__':
	main()