# code is situated in raspberry pi

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import datetime
import json

host = 'localhost'
commandTopic = 'RACK1'
sensorsTopic = 'RACK1S'
statusTopic = 'RACKSTATUS'
timeNow = ''
recipePath = 'planter_recipe.txt'
autoState = False
recipe_name, configuration, run_number, plant_type, led_type, start_date = '', '', '', '', '', ''

# irrigation
stage1Fill1, stage1Drain1, stage2Fill1, stage2Drain1, stage3Fill1, stage3Drain1 = [],[],[],[],[],[]
stage1Fill2, stage1Drain2, stage2Fill2, stage2Drain2, stage3Fill2, stage3Drain2 = [],[],[],[],[],[]

# light 1
stage1Led1On, stage1Led1Off, stage2Led1On, stage2Led1Off, stage3Led1On, stage3Led1Off = [],[],[],[],[],[]
stage1Led1Pwr, stage1Led1Dist, stage2Led1Pwr, stage2Led1Dist, stage3Led1Pwr, stage3Led1Dist = 0,0,0,0,0,0

# light 2
stage1Led2On, stage1Led2Off, stage2Led2On, stage2Led2Off, stage3Led2On, stage3Led2Off = [],[],[],[],[],[]
stage1Led2Pwr, stage1Led2Dist, stage2Led2Pwr, stage2Led2Dist, stage3Led2Pwr, stage3Led2Dist = 0,0,0,0,0,0

# doser
stage1Topup, stage2Topup, stage3Topup = [],[],[]
stage1Dose, stage2Dose, stage3Dose = [],[],[]
stage1Ec, stage2Ec, stage3Ec = 0.0, 0.0, 0.0
ec = 0.0
tankSize = 6000

# stage control
stage1Duration, stage2Duration, stage3Duration = 0, 0, 0
currentStage, daysPassed = 0, 0

 
def on_connect(client, userdata, flags, rc):
    client.subscribe(sensorsTopic)

def on_message(client, userdata, msg):
    message = str(msg.payload)
    message = message[2:-1]
    FilterIncomingMessage(message)

def FilterIncomingMessage(rawMessage):
	global ec
	message = rawMessage.split(' ')
	key = message[0]
	value = float(message[1])
	if key == 'CLK':
		Tick()
	if key == 'LOAD':
		LoadRecipe()
	if key == 'STATE':
		ChangeState()
	if key == 'EC':
		ec = value
	if key == 'AEC':
		ec = value
		DoserEcDose(ec)

def Tick():
	global timeNow, daysPassed,currentStage
	timeNow = time.strftime('%H:%M:%S')
	StatusCheck()
	IrrigationCheck1()
	IrrigationCheck2()
	LightCheck1()
	LightCheck2()
	DoserCheck()
	print (timeNow)

def StatusCheck():
	DaysPassedFunction()
	CurrentStageFunction()
	jsonStatusMessage = {
		'name': 'status',
		'daysPassed':daysPassed,
		'currentStage': currentStage
	}
	PublishJsonFormat(jsonStatusMessage,statusTopic)

def ParametersCheck():
	global recipe_name, configuration, run_number, plant_type, led_type, start_date
	jsonParameters = {
		'name': 'parameters',
		'recipe_name':recipe_name,
		'configuration':configuration,
		'run_number':run_number,
		'plant_type': plant_type,
		'led_type':led_type,
		'start_date':start_date
		}
	print(jsonParameters)
	PublishJsonFormat(jsonParameters,statusTopic)

def IrrigationCheck1():
	global autoState, currentStage, timeNow
	if autoState:
		if currentStage == 1:
			for thisTime in stage1Fill1:
				if thisTime == timeNow:
					PumpFunction(1,1)
			for thisTime in stage1Drain1:
				if thisTime == timeNow:
					DrainFunction(1,1)
		elif currentStage == 2:
			for thisTime in stage2Fill1:
				if thisTime == timeNow:
					PumpFunction(1,1)
			for thisTime in stage2Drain1:
				if thisTime == timeNow:
					DrainFunction(1,1)
		elif currentStage == 3:
			for thisTime in stage3Fill1:
				if thisTime == timeNow:
					PumpFunction(1,1)
			for thisTime in stage3Drain1:
				if thisTime == timeNow:
					DrainFunction(1,1)

def IrrigationCheck2():
	global autoState, currentStage, timeNow
	if autoState:
		if currentStage == 1:
			for thisTime in stage1Fill2:
				if thisTime == timeNow:
					PumpFunction(2,1)
			for thisTime in stage1Drain2:
				if thisTime == timeNow:
					DrainFunction(2,1)
		elif currentStage == 2:
			for thisTime in stage2Fill2:
				if thisTime == timeNow:
					PumpFunction(2,1)
			for thisTime in stage2Drain2:
				if thisTime == timeNow:
					DrainFunction(2,1)
		elif currentStage == 3:
			for thisTime in stage3Fill2:
				if thisTime == timeNow:
					PumpFunction(2,1)
			for thisTime in stage3Drain2:
				if thisTime == timeNow:
					DrainFunction(2,1)

def LightCheck1():
	global autoState, currentStage, timeNow
	global stage1Led1Pwr, stage2Led1Pwr, stage3Led1Pwr
	if autoState:
		if currentStage == 1:
			for thisTime in stage1Led1On:
				if thisTime == timeNow:
					LightPwrFunction(1,stage1Led1Pwr)
					time.sleep(2)
					LightDistanceFunction(1,stage1Led1Dist)
			for thisTime in stage1Led1Off:
				if thisTime == timeNow:
					LightPwrFunction(1,0)
		elif currentStage == 2:
			for thisTime in stage2Led1On:
				if thisTime == timeNow:
					LightPwrFunction(1,stage2Led1Pwr)
					time.sleep(2)
					LightDistanceFunction(1,stage2Led1Dist)
			for thisTime in stage2Led1Off:
				if thisTime == timeNow:
					LightPwrFunction(1,0)
		elif currentStage == 3:
			for thisTime in stage3Led1On:
				if thisTime == timeNow:
					LightPwrFunction(1,stage3Led1Pwr)
					time.sleep(2)
					LightDistanceFunction(1,stage3Led1Dist)
			for thisTime in stage3Led1Off:
				if thisTime == timeNow:
					LightPwrFunction(1,0)

def LightCheck2():
	global autoState, currentStage, timeNow
	global stage1Led2Pwr, stage2Led2Pwr, stage3Led2Pwr
	if autoState:
		if currentStage == 1:
			for thisTime in stage1Led2On:
				if thisTime == timeNow:
					LightPwrFunction(2,stage1Led2Pwr)
					time.sleep(2)
					LightDistanceFunction(2,stage1Led2Dist)
			for thisTime in stage1Led2Off:
				if thisTime == timeNow:
					LightPwrFunction(2,0)
		elif currentStage == 2:
			for thisTime in stage2Led2On:
				if thisTime == timeNow:
					LightPwrFunction(2,stage2Led2Pwr)
					time.sleep(2)
					LightDistanceFunction(2,stage2Led2Dist)
			for thisTime in stage2Led2Off:
				if thisTime == timeNow:
					LightPwrFunction(2,0)
		elif currentStage == 3:
			for thisTime in stage3Led2On:
				if thisTime == timeNow:
					LightPwrFunction(2,stage3Led2Pwr)
					time.sleep(2)
					LightDistanceFunction(2,stage3Led2Dist)
			for thisTime in stage3Led1Off:
				if thisTime == timeNow:
					LightPwrFunction(2,0)

def DoserCheck():
	global autoState, currentStage, timeNow
	if autoState:
		if currentStage == 1:
			for thisTime in stage1Topup:
				if thisTime == timeNow:
					DoserTopUpFunction(1)
			for thisTime in stage1Dose:
				if thisTime == timeNow:
					DoserEcDoseFunction()
		if currentStage == 2:
			for thisTime in stage2Topup:
				if thisTime == timeNow:
					DoserTopUpFunction(1)
			for thisTime in stage2Dose:
				if thisTime == timeNow:
					DoserEcDoseFunction()
		if currentStage == 3:
			for thisTime in stage3Topup:
				if thisTime == timeNow:
					DoserTopUpFunction(1)
			for thisTime in stage3Dose:
				if thisTime == timeNow:
					DoserEcDoseFunction()

def PumpFunction(channel,state):
	PublishStringFormat('PU{} {}'.format(channel,state))

def DrainFunction(channel,state):
	PublishStringFormat('DR{} {}'.format(channel,state))

def LightPwrFunction(channel,power):
	PublishStringFormat('LP{} {}'.format(channel,power))

def LightDistanceFunction(channel,distance):
	PublishStringFormat('LD{} {}'.format(channel,distance))

def DoserTopUpFunction():
	PublishStringFormat('PU {}'.format(state))

def DoserEcDoseFunction():
	PublishStringFormat('AEC 1')

def DoserEcDose(ecValue):
	global stage1Ec, stage2Ec, stage3Ec, tankSize
	nutrientVolume = 0
	EcFactor = 100.0
	if ecValue == 0 or ecValue == 100:
		nutrientVolume = 0
	elif currentStage == 1:
		nutrientVolume = (stage1Ec - ecValue) * float(tankSize / EcFactor)
	elif currentStage == 2:
		nutrientVolume = (stage2Ec - ecValue) * float(tankSize / EcFactor)
	elif currentStage == 3:
		nutrientVolume = (stage3Ec - ecValue) * float(tankSize / EcFactor)
	nutrientVolume = int(round(nutrientVolume))
	if nutrientVolume <= 0:
		pass
	else:
		print(nutrientVolume)
		PublishStringFormat('NP {}'.format(nutrientVolume/2))

def LoadRecipe():
	try:
		with open(recipePath,'r') as file:
			recipeContent = file.readlines()
	except:
		print('unable to find recipe file')
	else:
		ReadRecipe(recipeContent)

def ReadRecipe(recipeContent):
	global recipe_name, configuration, run_number, plant_type, led_type, start_date
	global stage1Fill1, stage1Drain1, stage2Fill1, stage2Drain1, stage3Fill1, stage3Drain1
	global stage1Led1On, stage1Led1Off, stage1Led1Pwr, stage1Led1Dist
	global stage2Led1On, stage2Led1Off, stage2Led1Pwr, stage2Led1Dist
	global stage3Led1On, stage3Led1Off, stage3Led1Pwr, stage3Led1Dist
	global stage1Fill2, stage1Drain2, stage2Fill2, stage2Drain2, stage3Fill2, stage3Drain2
	global stage1Led2On, stage1Led2Off, stage1Led2Pwr, stage1Led2Dist
	global stage2Led2On, stage2Led2Off, stage2Led2Pwr, stage2Led2Dist
	global stage3Led2On, stage3Led2Off, stage3Led2Pwr, stage3Led2Dist
	global stage1Topup, stage2Topup, stage3Topup
	global stage1Dose, stage2Dose, stage3Dose
	global stage1Ec,stage2Ec,stage3Ec
	global stage1Duration, stage2Duration, stage3Duration

	for line in range (0,len(recipeContent)):
		thisLine = recipeContent[line][:-1] # splice off \r\n
		try:
			thisLine = thisLine.split(' ') #split line into 2 items in an array
			parameter = thisLine[0] # allocate 1st item as parameter
			value = thisLine[1] # allocate 2nd items as value
		except:
			pass
		else:
			if parameter == 'recipe_name':
				recipe_name = value
			elif parameter == 'configuration':
				configuration = value
			elif parameter == 'run_number':
				run_number = value
			elif parameter == 'plant_type':
				plant_type = value
			elif parameter == 'led_type':
				led_type = value
			elif parameter == 'start_date':
				start_date = value
				'''channel 1'''
			elif parameter == 'stage1_fill1':
				stage1Fill1 = value.split(',')
			elif parameter == 'stage1_drain1':
				stage1Drain1 = value.split(',')
			elif parameter == 'stage2_fill1':
				stage2Fill1 = value.split(',')
			elif parameter == 'stage2_drain1':
				stage2Drain1 = value.split(',')
			elif parameter == 'stage3_fill1':
				stage3Fill1 = value.split(',')
			elif parameter == 'stage3_drain1':
				stage3Drain1 = value.split(',')
			elif parameter == 'stage1_led1_on':
				stage1Led1On = value.split(',')
			elif parameter == 'stage1_led1_off':
				stage1Led1Off = value.split(',')
			elif parameter == 'stage1_led1_pwr':
				stage1Led1Pwr = int(value)
			elif parameter == 'stage1_led1_dist':
				stage1Led1Dist = int(value)
			elif parameter == 'stage2_led1_on':
				stage2Led1On = value.split(',')
			elif parameter == 'stage2_led1_off':
				stage2Led1Off = value.split(',')
			elif parameter == 'stage2_led1_pwr':
				stage2Led1Pwr = int(value)
			elif parameter == 'stage2_led1_dist':
				stage2Led1Dist = int(value)
			elif parameter == 'stage3_led1_on':
				stage3Led1On = value.split(',')
			elif parameter == 'stage3_led1_off':
				stage3Led1Off = value.split(',')
			elif parameter == 'stage3_led1_pwr':
				stage3Led1Pwr = int(value)
			elif parameter == 'stage3_led1_dist':
				stage3Led1Dist = int(value)
				'''channel 2'''
			elif parameter == 'stage1_fill2':
				stage1Fill2 = value.split(',')
			elif parameter == 'stage1_drain2':
				stage1Drain2 = value.split(',')
			elif parameter == 'stage2_fill2':
				stage2Fill2 = value.split(',')
			elif parameter == 'stage2_drain2':
				stage2Drain2 = value.split(',')
			elif parameter == 'stage3_fill2':
				stage3Fill2 = value.split(',')
			elif parameter == 'stage3_drain2':
				stage3Drain2 = value.split(',')
			elif parameter == 'stage1_led2_on':
				stage1Led2On = value.split(',')
			elif parameter == 'stage1_led2_off':
				stage1Led2Off = value.split(',')
			elif parameter == 'stage1_led2_pwr':
				stage1Led2Pwr = int(value)
			elif parameter == 'stage1_led2_dist':
				stage1Led2Dist = int(value)
			elif parameter == 'stage2_led2_on':
				stage2Led2On = value.split(',')
			elif parameter == 'stage2_led2_off':
				stage2Led2Off = value.split(',')
			elif parameter == 'stage2_led2_pwr':
				stage2Led2Pwr = int(value)
			elif parameter == 'stage2_led2_dist':
				stage2Led2Dist = int(value)
			elif parameter == 'stage3_led2_on':
				stage3Led2On = value.split(',')
			elif parameter == 'stage3_led2_off':
				stage3Led2Off = value.split(',')
			elif parameter == 'stage3_led2_pwr':
				stage3Led2Pwr = int(value)
			elif parameter == 'stage3_led2_dist':
				stage3Led2Dist = int(value)

			elif parameter == 'stage1_ec':
				stage1Ec = float(value)
			elif parameter == 'stage1_topup':
				stage1Topup = value.split(',')
			elif parameter == 'stage1_dose':
				stage1Dose = value.split(',')
			elif parameter == 'stage2_ec':
				stage2Ec = float(value)
			elif parameter == 'stage2_topup':
				stage2Topup = value.split(',')
			elif parameter == 'stage2_dose':
				stage2Dose = value.split(',')
			elif parameter == 'stage3_ec':
				stage3Ec = float(value)
			elif parameter == 'stage3_topup':
				stage3Topup = value.split(',')
			elif parameter == 'stage3_dose':
				stage3Dose = value.split(',')
			elif parameter == 'stage1_duration':
				stage1Duration = int(value)
			elif parameter == 'stage2_duration':
				stage2Duration = int(value)
			elif parameter == 'stage3_duration':
				stage3Duration = int(value)
	ParametersCheck()

def ChangeState():
	global autoState
	autoState = not autoState
	if autoState:
		PublishStringFormat('STATE 1')
	else:
		PublishStringFormat('STATE 0')
	print ('STATE: {}'.format(autoState))

def DaysPassedFunction():
	global start_date, daysPassed
	today = datetime.date.today()
	start_date_formatted = start_date.split('/')
	try:
		day=int(start_date_formatted[0])
		month=int(start_date_formatted[1])
		year=int(start_date_formatted[2])
	except:
		pass
	else:
		dateStart = datetime.date(year,month,day)
		daysPassed = (today-dateStart).days

def CurrentStageFunction():
	global daysPassed, stage1Duration, stage2Duration, stage3Duration, currentStage
	if daysPassed <= stage1Duration:
		currentStage = 1
	elif stage1Duration <= daysPassed <= (stage1Duration + stage2Duration):
		currentStage = 2
	elif (stage1Duration + stage2Duration) <= daysPassed <= (stage1Duration + stage2Duration\
	+ stage3Duration):
		currentStage = 3
	else:
		currentStage = 3

def PublishJsonFormat(jsonMessage,topic):
	formattedJson = json.dumps(jsonMessage)
	publish.single(topic, formattedJson, hostname=host)

def PublishStringFormat(stringMessage):
	publish.single(commandTopic, stringMessage, hostname=host)

def InitialCheck():
	jsonStatusMessage = {
		'name': 'status',
		'daysPassed':'',
		'currentStage': ''
	}
	PublishJsonFormat(jsonStatusMessage,statusTopic)

def main():
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host, 1883, 60)
	ParametersCheck()
	InitialCheck()
	client.loop_forever()

if __name__ == '__main__':
	main()
