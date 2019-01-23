import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import time
import datetime

host = '10.42.0.137' 
recipeTopic = 'planter_recipe'
commandTopic = 'planter_command'
recipe1a = {}
recipe1b = {}
recipe1c = {}
recipe2a = {}
recipe2b = {}
recipe2c = {}
recipeMain = {}
currentStage = 0
autoMode = False
tankSize = 6000
 
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe(recipeTopic)
 
def on_message(client, userdata, msg):
	global recipeMain, recipe1a, recip1eb, recipe1c, recipe2a, recipe2b, recipe2c
	decodedMessage = str(msg.payload.decode("utf-8","ignore"))
	message = json.loads(decodedMessage)
	if message["topic"] == "recipe":
		if message["channel"] == 1:
			if message["stage"] == 1:
				recipe1a = message
			elif message["stage"] == 2:
				recipe1b = message
			elif message["stage"] == 3:
				recipe1c = message
		elif message["channel"] == 2:
			if message["stage"] == 1:
				recipe2a = message
			elif message["stage"] == 2:
				recipe2b = message
			elif message["stage"] == 3:
				recipe2c = message
		indentedRecipe = json.dumps(message, indent = 2, sort_keys = True)
		print(indentedRecipe) # print a nicely indented json format
	elif message["topic"] == "recipeMain":
		recipeMain = message
		print (recipeMain)
		DaysPassedStageCheck()
	elif message["topic"] == "clock":
		Tick()
	elif message["topic"] == "AEC":
		ec = message["ec"]
		Dose(float(ec))
		print('dose activate')

def Tick():
	global timeNow, autoMode
	timeNow = time.strftime("%H:%M:%S")
	CheckAutoMode()
	IrrigationCheck1()
	IrrigationCheck2()
	LightCheck1()
	LightCheck2()
	DoserCheck()

def CheckAutoMode():
	global autoMode, recipeMain
	try:
		if recipeMain['autoMode'] == True:
			autoMode = True
		else: 
			autoMode = False
	except:
		pass

def DaysPassedStageCheck():
	global recipeMain
	today = datetime.date.today()
	try:
		start_date_formatted = recipeMain['startDate'].split('/')
		day=int(start_date_formatted[0])
		month=int(start_date_formatted[1])
		year=int(start_date_formatted[2])
	except:
		print('no date!')
	else:
		dateStart = datetime.date(year,month,day)
		daysPassed = (today-dateStart).days
		PublishStringFormat('DAYS {}'.format(daysPassed))
		CurrentStageCheck(daysPassed)

def CurrentStageCheck(daysPassed):
	global recipeMain, currentStage
	try:
		stage1Duration = recipeMain['stage1Duration']
		stage2Duration = recipeMain['stage2Duration']
		stage3Duration = recipeMain['stage3Duration']
	except:
		pass
	else:
		if daysPassed <= stage1Duration:
			currentStage = 1
		elif stage1Duration <= daysPassed <= (stage1Duration + stage2Duration):
			currentStage = 2
		elif (stage1Duration + stage2Duration) <= daysPassed <= (stage1Duration + stage2Duration\
		+ stage3Duration):
			currentStage = 3
		else:
			currentStage = 3
		PublishStringFormat('STAGE {}'.format(currentStage))

def IrrigationCheck1():
	global timeNow, recipe1a, recipe1b, recipe1c, currentStage, autoMode
	if autoMode:
		if currentStage == 1:
			for thisTime in recipe1a['fill']:
				if thisTime == timeNow:
					PublishStringFormat('PU1 1')
			for thisTime in recipe1a['drain']:
				if thisTime == timeNow:
					PublishStringFormat('DR1 1')
		elif currentStage == 2:
			for thisTime in recipe1b['fill']:
				if thisTime == timeNow:
					PublishStringFormat('PU1 1')
			for thisTime in recipe1b['drain']:
				if thisTime == timeNow:
					PublishStringFormat('DR1 1')
		elif currentStage == 3:
			for thisTime in recipe1c['fill']:
				if thisTime == timeNow:
					PublishStringFormat('PU1 1')
			for thisTime in recipe1c['drain']:
				if thisTime == timeNow:
					PublishStringFormat('DR1 1')

def IrrigationCheck2():
	global timeNow, recipe2a, recipe2b, recipe2c, currentStage, autoMode
	if autoMode:
		if currentStage == 1:
			for thisTime in recipe2a['fill']:
				if thisTime == timeNow:
					PublishStringFormat('PU2 1')
			for thisTime in recipe2a['drain']:
				if thisTime == timeNow:
					PublishStringFormat('DR2 1')
		elif currentStage == 2:
			for thisTime in recipe2b['fill']:
				if thisTime == timeNow:
					PublishStringFormat('PU2 1')
			for thisTime in recipe2b['drain']:
				if thisTime == timeNow:
					PublishStringFormat('DR2 1')
		elif currentStage == 3:
			for thisTime in recipe2c['fill']:
				if thisTime == timeNow:
					PublishStringFormat('PU2 1')
			for thisTime in recipe2c['drain']:
				if thisTime == timeNow:
					PublishStringFormat('DR2 1')

def LightCheck1():
	global timeNow, recipe1a, recipe1b, recipe1c, currentStage, autoMode
	try:
		stage1LightPower = recipe1a['lightPwr']
		stage2LightPower = recipe1b['lightPwr']
		stage3LightPower = recipe1c['lightPwr']
		stage1LightDistance = recipe1a['lightDist']
		stage2LightDistance = recipe1b['lightDist']
		stage3LightDistance = recipe1c['lightDist']
	except:
		pass
	else:
		if autoMode:
			if currentStage == 1:
				for thisTime in recipe1a['lightOn']:
					if thisTime == timeNow:
						PublishStringFormat('LP1 {}'.format(stage1LightPower))
						time.sleep(2)
						PublishStringFormat('LD1 {}'.format(stage1LightDistance))
				for thisTime in recipe1a['lightOff']:
					if thisTime == timeNow:
						PublishStringFormat('LP1 0')
			elif currentStage == 2:
				for thisTime in recipe1b['lightOn']:
					if thisTime == timeNow:
						PublishStringFormat('LP1 {}'.format(stage2LightPower))
						time.sleep(2)
						PublishStringFormat('LD1 {}'.format(stage2LightDistance))
				for thisTime in recipe1b['lightOff']:
					if thisTime == timeNow:
						PublishStringFormat('LP1 0')
			elif currentStage == 3:
				for thisTime in recipe1c['lightOn']:
					if thisTime == timeNow:
						PublishStringFormat('LP1 {}'.format(stage3LightPower))
						time.sleep(2)
						PublishStringFormat('LD1 {}'.format(stage3LightDistance))
				for thisTime in recipe1c['lightOff']:
					if thisTime == timeNow:
						PublishStringFormat('LP1 0')

def LightCheck2():
	global timeNow, recipe2a, recipe2b, recipe2c, currentStage, autoMode
	try:
		stage1LightPower = recipe2a['lightPwr']
		stage2LightPower = recipe2b['lightPwr']
		stage3LightPower = recipe2c['lightPwr']
		stage1LightDistance = recipe2a['lightDist']
		stage2LightDistance = recipe2b['lightDist']
		stage3LightDistance = recipe2c['lightDist']
	except:
		pass
	else:
		if autoMode:
			if currentStage == 1:
				for thisTime in recipe2a['lightOn']:
					if thisTime == timeNow:
						PublishStringFormat('LP2 {}'.format(stage1LightPower))
						time.sleep(2)
						PublishStringFormat('LD2 {}'.format(stage1LightDistance))
				for thisTime in recipe2a['lightOff']:
					if thisTime == timeNow:
						PublishStringFormat('LP2 0')
			elif currentStage == 2:
				for thisTime in recipe2b['lightOn']:
					if thisTime == timeNow:
						PublishStringFormat('LP2 {}'.format(stage2LightPower))
						time.sleep(2)
						PublishStringFormat('LD2 {}'.format(stage2LightDistance))
				for thisTime in recipe2b['lightOff']:
					if thisTime == timeNow:
						PublishStringFormat('LP2 0')
			elif currentStage == 3:
				for thisTime in recipe2c['lightOn']:
					if thisTime == timeNow:
						PublishStringFormat('LP2 {}'.format(stage3LightPower))
						time.sleep(2)
						PublishStringFormat('LD2 {}'.format(stage3LightDistance))
				for thisTime in recipe2c['lightOff']:
					if thisTime == timeNow:
						PublishStringFormat('LP2 0')

def DoserCheck():
	global autoMode, timeNow
	if autoMode:
		if timeNow == '21:00:00':
			PublishStringFormat('PU 1')
		if timeNow == '21:30:00':
			PublishStringFormat('AEC 1')

def Dose(ec):
	global recipeMain, currentStage, tankSize
	try:
		stage1Ec = recipeMain['stage1Ec']
		stage2Ec = recipeMain['stage2Ec']
		stage3Ec = recipeMain['stage3Ec']
	except:
		print('dose error')
	else:
		nutrientVolume = 0
		ecFactor = 100.0
		if ec == 0 or ec == 100:
			nutrientVolume = 0
		elif currentStage == 1:
			nutrientVolume = (stage1Ec - ec) * float(tankSize / ecFactor)
		elif currentStage == 2:
			nutrientVolume = (stage2Ec - ec) * float(tankSize / ecFactor)
		elif currentStage == 3:
			nutrientVolume = (stage3Ec - ec) * float(tankSize / ecFactor)
		nutrientVolume = int(round(nutrientVolume))
		if nutrientVolume <= 0:
			pass
		else:
			PublishStringFormat('NP {}'.format(nutrientVolume/2))
			print(nutrientVolume)

def PublishStringFormat(stringMessage):
	publish.single(commandTopic, stringMessage, hostname=host)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host,1883,60)
client.loop_forever()
