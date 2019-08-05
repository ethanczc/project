from PlanterComponents import Pump, Led, Doser
import json
import time

recipe = {}

pump = Pump(17)
led = Led(27)
doser = Doser(22,23,50,50)

timeNow = time.strftime('%H:%M:%S')
print(timeNow)

def Read_Recipe():
	global recipe
	try:
		with open('recipe.js') as file:
			recipe = json.load(file)
			#print (recipe)
	except:
		print('no file found')

def PumpCheck():
	Read_Recipe()
	global recipe, timeNow
	for thisTime in recipe['pumpOn']:
		if thisTime == timeNow:
			pump.On()
	for thisTime in recipe['pumpOff']:
		if thisTime == timeNow:
			pump.Off()

def LightCheck():
	Read_Recipe()
	global recipe, timeNow
	for thisTime in recipe['lightOn']:
		if thisTime == timeNow:
			led.On()
	for thisTime in recipe['lightOff']:
		if thisTime == timeNow:
			led.Off()

def DoseCheck():
	Read_Recipe()
	global recipe, timeNow
	for thisTime in recipe['dose']:
		if thisTime == timeNow:
			print('turning dosing on')
			Dose()
		else:
			print('not yet turn doser on')

def Dose():
	Read_Recipe()
	doser.Read()
	print (recipe['mixRatio'])
	if recipe['ec'] > doser.measuredEC :
		dosingVolume = (recipe['ec']-doser.measuredEC) * recipe['tankVol'] * recipe['mixRatio']
		doser.Dose(dosingVolume)

def main():
	LightCheck()
	PumpCheck()
	DoseCheck()
	Dose()

if __name__ == '__main__':
	main()