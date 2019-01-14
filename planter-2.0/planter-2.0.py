import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import time

host = '10.42.0.137' 
recipeTopic = 'planter_recipe'
recipe = {}
 
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe(recipeTopic)
 
def on_message(client, userdata, msg):
	global recipe
	decodedMessage = str(msg.payload.decode("utf-8","ignore"))
	message = json.loads(decodedMessage)
	if message["topic"] == "recipe":
		recipe = message
		indentedRecipe = json.dumps(message, indent = 2, sort_keys = True)
		print(indentedRecipe) # print a nicely indented json format
	elif message ["topic"] == "clock":
		Tick()

def Tick():
	global timeNow
	timeNow = time.strftime("%H:%M:%S")
	print(timeNow)
	IrrigationCheck()

def IrrigationCheck():
	global timeNow, recipe
	for thisTime in recipe['stage1Fill']:
		if thisTime == timeNow:
			print('tio')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host,1883,60)
client.loop_forever()
