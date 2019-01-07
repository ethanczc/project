# code is situated in raspberry pi

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import datetime
import json

host = '10.42.0.137'
commandTopic = 'RACK1'
sensorsTopic = 'RACK1S'
statusTopic = 'RACKSTATUS'
timeNow = ''
recipePath = 'planter_recipe.txt'
autoState = True
recipe_name, configuration, run_number, plant_type, led_type, start_date = '', '', '', '', '', ''
stage1Fill1, stage1Drain1, stage2Fill1, stage2Drain1, stage3Fill1, stage3Drain1 = [],[],[],[],[],[]
stage1Fill2, stage1Drain2, stage2Fill2, stage2Drain2, stage3Fill2, stage3Drain2 = [],[],[],[],[],[]
stage1Led1On, stage1Led1Off = [], []
stage1Led1Pwr, stage1Led1Dist = 0, 0
stage2Led1On, stage2Led1Off = [], []
stage2Led1Pwr, stage2Led1Dist = 0, 0
stage3Led1On, stage3Led1Off = [], []
stage3Led1Pwr, stage3Led1Dist = 0, 0
stage1Led2On, stage1Led2Off = [], []
stage1Led2Pwr, stage1Led2Dist = 0, 0
stage2Led2On, stage2Led2Off = [], []
stage2Led2Pwr, stage2Led2Dist = 0, 0
stage3Led2On, stage3Led2Off = [], []
stage3Led2Pwr, stage3Led2Dist = 0, 0
stage1Duration, stage2Duration, stage3Duration = 0, 0, 0
currentStage, daysPassed = 0, 0
 
def on_connect(client, userdata, flags, rc):
    client.subscribe(sensorsTopic)

def on_message(client, userdata, msg):
    message = str(msg.payload)
    message = message[2:-1]
    DecodeMessage(message)

def DecodeMessage(rawMessage):
	message = rawMessage.split(' ')
	if message[0] == 'CLK':
		Tick()
	if message[0] == 'LOAD':
		LoadRecipe()
	if message[0] == 'STATE':
		ChangeState()

def Tick():
	global timeNow
	timeNow = time.strftime('%H:%M:%S')
	print (timeNow)
	DaysPassedDisplay()
	CurrentStageDisplay()
	jsonStatusMessage = {
		'daysPassed':daysPassed,
		'currentStage': currentStage
	}
	PublishJsonFormat(jsonStatusMessage,statusTopic)

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
	jsonStatus = {
			'recipe_name':recipe_name,
			'configuration':configuration,
			'run_number':run_number,
			'plant_type': plant_type,
			'led_type':led_type,
			'start_date':start_date
			}
	print(jsonStatus)
	PublishJsonFormat(jsonStatus,commandTopic)

def ChangeState():
	global autoState
	autoState = not autoState
	if autoState:
		PublishStringFormat('STATE 1')
	else:
		PublishStringFormat('STATE 0')

def DaysPassedDisplay():
	global start_date, daysPassed
	today = datetime.date.today()
	start_date_formatted = start_date.split('/')
	day=int(start_date_formatted[0])
	month=int(start_date_formatted[1])
	year=int(start_date_formatted[2])
	dateStart = datetime.date(year,month,day)
	daysPassed = (today-dateStart).days

def CurrentStageDisplay():
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

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, 1883, 60)
client.loop_forever()
