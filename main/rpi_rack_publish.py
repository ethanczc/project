import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import serial
import time

host = '10.42.0.1' #ip address of host computer
commandTopic = 'RACK1' # topic name to suscribe to
sensorsTopic = 'RACK1S' # topic to publish to

serial_3 = False

try:
	ser3 = serial.Serial('/dev/ttyUSB2',9600)
except:
	pass
else:
	serial_3 = True
	print('ser3 ok')

def ListenSerial():
	'''seperate thread to listen to serial doser for AEC and EC feedback and pass to computer
		also to listen to serial irrigation for PWS (photoelectric water sensor)'''
	global ser3
	while True:
		print('thread running')
		time.sleep(1)
		try:
			rawData = ser3.readline()
			rawData = rawData.decode('utf-8')
			rawData = rawData[:-2]
			data = rawData.split(' ')
			
		except:
			pass
		else:
			if data[0] == 'PWS' or data[0] == 'AEC' or data[0] == 'EC':
				publish.single(sensorsTopic,rawData,hostname=host)
			print(rawData)

ListenSerial()