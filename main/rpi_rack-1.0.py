import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import serial
import time
import threading

'''
MQTT to serial handler for Raspberry Pi
Headless display, SSH from computer
plug in USB ports as follows:
	/dev/ttyUSB0 -> irrigation
	/dev/ttyUSB1 -> LED
	/dev/ttyUSB2 -> doser
identify port addresses and ensure sequence is accurate before running code
'''

host = '10.42.0.1' #ip address of host computer
commandTopic = 'RACK1' # topic name to suscribe to
sensorsTopic = 'RACK1S' # topic to publish to

serial_1 = False
serial_2 = False
serial_3 = False

try:
	ser1 = serial.Serial('/dev/ttyUSB0',9600)
except:
	pass
else:
	serial_1 = True
	print('ser1 ok')
try:
	ser2 = serial.Serial('/dev/ttyUSB1',9600)
except:
	pass
else:
	serial_2 = True
	print('ser2 ok')
try:
	ser3 = serial.Serial('/dev/ttyUSB2',9600)
except:
	pass
else:
	serial_3 = True
	print('ser3 ok')
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(commandTopic)
 
def on_message(client, userdata, msg):
	messageRecieved = str(msg.payload)
	messageRecieved = messageRecieved[2:-1]
	Decode_Message(messageRecieved)

def Decode_Message(message):
	data = message.split(' ')
	dataType = data[0]
	dataValue = data[1]
	CheckData(dataType,dataValue)

def CheckData(dataType,dataValue):
	'''check MQTT message and divert to relevant serial ports'''
	message = '{} {}'.format(dataType,dataValue)

	if serial_1 == True:
		if dataType == 'PU1' or dataType == 'PU2' or dataType == 'PU3' or dataType == 'PU4'\
		or dataType == 'DR1' or dataType == 'DR2' or dataType == 'DR3' or dataType == 'DR4'\
		or dataType == 'PU0' or dataType == 'DR0':
			print('ser1: {}'.format(message))
			ser1.write(message.encode())
		
	if serial_2 == True:
		if dataType == 'LP1' or dataType == 'LP2' or dataType == 'LP3' or dataType == 'LP4'\
		or dataType == 'LD1' or dataType == 'LD2' or dataType == 'LD3' or dataType == 'LD4'\
		or dataType == 'LD0' or dataType == 'LP0' or dataType == 'EN' or dataType == 'DA'\
		or dataType == 'HM':
			print('ser2: {}'.format(message))
			ser2.write(message.encode())

	if serial_3 == True:
		if dataType == 'NP' or dataType == 'EC' or dataType == 'AEC' or dataType == 'PU'\
		or dataType == 'AP' or dataType == 'BP' or dataType == 'NPA' or dataType == 'NPB':
			print('ser3: {}'.format(message))
			ser3.write(message.encode())

	else:
		print('unknown command: {} {}'.format(dataType,dataValue))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, 1883, 60)
client.loop_forever()
