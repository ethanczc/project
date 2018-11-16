import wx
import gui_main_e1_0 as gui
import time
import datetime
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
'''
new version from 2.0
Now uses MQTT to issue commands to a command topic 'RACK1'
and listens to sensors topic 'RACK1S'
'''

class Irrigation(gui.GuiFrame):
	def __init__(self,parent):
		gui.GuiFrame.__init__(self,parent)
		self.timeNow, self.dateNow = '', ''
		self.logFile = ''
		self.commandTopic = ''
		self.sensorsTopic = ''
		self.host = ''
		self.client = mqtt.Client()

		self.light1_stage1_on, self.light1_stage1_off = [], []
		self.light1_stage2_on, self.light1_stage2_off = [], []
		self.light1_stage3_on, self.light1_stage3_off = [], []

		self.light2_stage1_on, self.light2_stage1_off = [], []
		self.light2_stage2_on, self.light2_stage2_off = [], []
		self.light2_stage3_on, self.light2_stage3_off = [], []

		self.ch1_stage1_pump, self.ch1_stage1_drain = [], []
		self.ch1_stage2_pump, self.ch1_stage2_drain = [], []
		self.ch1_stage3_pump, self.ch1_stage3_drain = [], []

		self.ch2_stage1_pump, self.ch2_stage1_drain = [], []
		self.ch2_stage2_pump, self.ch2_stage2_drain = [], []
		self.ch2_stage3_pump, self.ch2_stage3_drain = [], []

		''' dwc-added construct start'''

		self.dwcLight_stage1_power, self.dwcLight_stage1_distance = 0, 0
		self.dwcLight_stage1_on, self.dwcLight_stage1_off = [], []

		self.dwcLight_stage2_power, self.dwcLight_stage2_distance = 0, 0
		self.dwcLight_stage2_on, self.dwcLight_stage2_off = [], []

		self.dwcLight_stage3_power, self.dwcLight_stage3_distance = 0, 0
		self.dwcLight_stage3_on, self.dwcLight_stage3_off = [], []

		self.dwcLight_stage1_duration, self.dwcLight_stage2_duration, self.dwcLight_stage3_duration = 0, 0, 0
		self.dwcLightCurrentStage = 0

		self.dwcTopup_frequency = 0
		self.dwcTopup_timing = []


		''' dwc-added construct ends '''

		self.tankSize = 0
		self.waterCheckTiming, self.ecCheckTiming = [], []
		self.stage1Ec, self.stage2Ec, self.stage3Ec = 0, 0, 0

		''' stages '''
		self.ch1_stage1_duration, self.ch1_stage2_duration, self.ch1_stage3_duration = 0, 0, 0
		self.ch2_stage1_duration, self.ch2_stage2_duration, self.ch2_stage3_duration = 0, 0, 0
		self.ch1CurrentStage, self.ch2CurrentStage = 0, 0

		self.temp1, self.temp2 = 0, 0
		self.humidity = 0
		self.ec = 0

	def Tick(self,parent):
		self.TimeDateDisplay()
		self.DaysPassedDisplay()
		self.IrrigationCheck()
		self.DoserCheck()
		self.LightCheck()
		self.UpdateSensors()

	def ConnectMQTT(self,event):
		self.host = self.hostIp_Txtctrl.GetValue()
		self.commandTopic = self.commandTopic_Txtctrl.GetValue()
		self.sensorsTopic = self.sensorsTopic_Txtctrl.GetValue()
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message
		self.client.connect(self.host, 1883, 60)
		self.client.loop_start()
		self.mqttStatus_Display.SetLabel('Connected')

	def SendMQTT(self,event):
		message = self.sendMqtt_Txtctrl.GetValue()
		publish.single(self.commandTopic,message,hostname=self.host)

	def on_connect(self,client, userdata, flags, rc):
	    self.client.subscribe(self.sensorsTopic)

	def on_message(self,client, userdata, msg):
		messageRecieved = str(msg.payload)
		messageRecieved = messageRecieved[2:-1]
		message = messageRecieved.split(' ')
		self.CheckMQTTMessage(message[0],message[1])

	def TimeDateDisplay(self):
		self.timeNow = time.strftime('%H:%M:%S')
		self.dateNow = time.strftime('%d/%m/%y')
		self.clock_Display.SetLabel(self.timeNow)
		self.date_Display.SetLabel(self.dateNow)

	def DaysPassedDisplay(self):
		today = datetime.date.today()
		try:
			dateStartInput = (self.startDate_Txtctrl.GetValue()).split('/')
			day = int(dateStartInput[0])
			month = int(dateStartInput[1])
			year = int(dateStartInput[2])
			dateStart = datetime.date(year,month,day)
			daysPassed = (today-dateStart).days
			self.daysPassed_Display.SetLabel(str(daysPassed))
		except:
			pass
		else:
			if daysPassed <= self.ch1_stage1_duration:
				self.ch1CurrentStage = 1
			elif self.ch1_stage1_duration <= daysPassed <= (self.ch1_stage1_duration + self.ch1_stage2_duration):
				self.ch1CurrentStage = 2
			elif (self.ch1_stage1_duration + self.ch1_stage2_duration) <= daysPassed <= (self.ch1_stage1_duration + self.ch1_stage2_duration\
			+ self.ch1_stage3_duration):
				self.ch1CurrentStage = 3
			else:
				self.ch1CurrentStage = 3
			self.ch1CurrentStage_Display.SetLabel(str(self.ch1CurrentStage))

			if daysPassed <= self.ch2_stage1_duration:
				self.ch2CurrentStage = 1
			elif self.ch2_stage1_duration <= daysPassed <= (self.ch2_stage1_duration + self.ch2_stage2_duration):
				self.ch2CurrentStage = 2
			elif (self.ch2_stage1_duration + self.ch2_stage2_duration) <= daysPassed <= (self.ch2_stage1_duration + self.ch2_stage2_duration\
			+ self.ch2_stage3_duration):
				self.ch2CurrentStage = 3
			else:
				self.ch2CurrentStage = 3
			self.ch2CurrentStage_Display.SetLabel(str(self.ch2CurrentStage))

			''' dwc-added stage calculation start'''
			if daysPassed <= self.dwcLight_stage1_duration:
				self.dwcLightCurrentStage = 1
			elif self.dwcLight_stage1_duration <= daysPassed <= (self.dwcLight_stage1_duration + self.dwcLight_stage2_duration):
				self.dwcLightCurrentStage = 2
			elif (self.dwcLight_stage1_duration + self.dwcLight_stage2_duration) <= daysPassed <= (self.dwcLight_stage1_duration + self.dwcLight_stage2_duration\
			+ self.dwcLight_stage3_duration):
				self.dwcLightCurrentStage = 3
			else:
				self.dwcLightCurrentStage = 3
			self.dwcLightCurrentStage_Display.SetLabel(str(self.dwcLightCurrentStage))
			''' dwc-added stage calculation end'''

	def LoadRecipe(self,event):
		with wx.FileDialog(self, "Open Text file", wildcard="Text files (*.txt)|*.txt",\
			style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			recipeFile = fileDialog.GetPath()
			try:
				with open(recipeFile, 'r') as file:
					recipeContent = file.readlines()
					self.ReadRecipe(recipeContent)
			except IOError:
				wx.LogError("Cannot open file '%s'." % newfile)

	def ReadRecipe(self,recipeContent):
		for line in range (0,len(recipeContent)):
			thisLine = recipeContent[line][:-1] # splice off \r\n
			thisLine = thisLine.split(' ') #split line into 2 items in an array
			parameter = thisLine[0] # allocate 1st item as parameter
			value = thisLine[1] # allocate 2nd items as value
			if parameter == 'recipe_name':
				self.recipe_Display.SetLabel(str(value))
			if parameter == 'configuration':
				self.config_Txtctrl.SetValue(value)
			if parameter == 'run_number':
				self.run_Txtctrl.SetValue(value)
			if parameter == 'plant_type':
				self.plant_Txtctrl.SetValue(value)
			if parameter == 'led_type':
				self.led_Txtctrl.SetValue(value)
			if parameter == 'start_date':
				self.startDate_Txtctrl.SetValue(value)
			if parameter == 'light1_stage1_on':
				self.light1_stage1_on = value.split(',')
				self.light1_stage1_on_Display.SetLabel(str(self.light1_stage1_on))
			if parameter == 'light1_stage1_off':
				self.light1_stage1_off = value.split(',')
				self.light1_stage1_off_Display.SetLabel(str(self.light1_stage1_off))
			if parameter == 'light1_stage2_on':
				self.light1_stage2_on = value.split(',')
				self.light1_stage2_on_Display.SetLabel(str(self.light1_stage2_on))
			if parameter == 'light1_stage2_off':
				self.light1_stage2_off = value.split(',')
				self.light1_stage2_off_Display.SetLabel(str(self.light1_stage2_off))
			if parameter == 'light1_stage3_on':
				self.light1_stage3_on = value.split(',')
				self.light1_stage3_on_Display.SetLabel(str(self.light1_stage3_on))
			if parameter == 'light1_stage3_off':
				self.light1_stage3_off = value.split(',')
				self.light1_stage3_off_Display.SetLabel(str(self.light1_stage3_off))
			if parameter == 'light2_stage1_on':
				self.light2_stage1_on = value.split(',')
				self.light2_stage1_on_Display.SetLabel(str(self.light2_stage1_on))
			if parameter == 'light2_stage1_off':
				self.light2_stage1_off = value.split(',')
				self.light2_stage1_off_Display.SetLabel(str(self.light2_stage1_off))
			if parameter == 'light2_stage2_on':
				self.light2_stage2_on = value.split(',')
				self.light2_stage2_on_Display.SetLabel(str(self.light2_stage2_on))
			if parameter == 'light2_stage2_off':
				self.light2_stage2_off = value.split(',')
				self.light2_stage2_off_Display.SetLabel(str(self.light2_stage2_off))
			if parameter == 'light2_stage3_on':
				self.light2_stage3_on = value.split(',')
				self.light2_stage3_on_Display.SetLabel(str(self.light2_stage3_on))
			if parameter == 'light2_stage3_off':
				self.light2_stage3_off = value.split(',')
				self.light2_stage3_off_Display.SetLabel(str(self.light2_stage3_off))
			if parameter == 'ch1_stage1_pump':
				self.ch1_stage1_pump = value.split(',')
				self.ch1_stage1_pump_Display.SetLabel(str(self.ch1_stage1_pump))
			if parameter == 'ch1_stage1_drain':
				self.ch1_stage1_drain = value.split(',')
				self.ch1_stage1_drain_Display.SetLabel(str(self.ch1_stage1_drain))
			if parameter == 'ch1_stage2_pump':
				self.ch1_stage2_pump = value.split(',')
				self.ch1_stage2_pump_Display.SetLabel(str(self.ch1_stage2_pump))
			if parameter == 'ch1_stage2_drain':
				self.ch1_stage2_drain = value.split(',')
				self.ch1_stage2_drain_Display.SetLabel(str(self.ch1_stage2_drain))
			if parameter == 'ch1_stage3_pump':
				self.ch1_stage3_pump = value.split(',')
				self.ch1_stage3_pump_Display.SetLabel(str(self.ch1_stage3_pump))
			if parameter == 'ch1_stage3_drain':
				self.ch1_stage3_drain = value.split(',')
				self.ch1_stage3_drain_Display.SetLabel(str(self.ch1_stage3_drain))
			if parameter == 'ch2_stage1_pump':
				self.ch2_stage1_pump = value.split(',')
				self.ch2_stage1_pump_Display.SetLabel(str(self.ch2_stage1_pump))
			if parameter == 'ch2_stage1_drain':
				self.ch2_stage1_drain = value.split(',')
				self.ch2_stage1_drain_Display.SetLabel(str(self.ch2_stage1_drain))
			if parameter == 'ch2_stage2_pump':
				self.ch2_stage2_pump = value.split(',')
				self.ch2_stage2_pump_Display.SetLabel(str(self.ch2_stage2_pump))
			if parameter == 'ch2_stage2_drain':
				self.ch2_stage2_drain = value.split(',')
				self.ch2_stage2_drain_Display.SetLabel(str(self.ch2_stage2_drain))
			if parameter == 'ch2_stage3_pump':
				self.ch2_stage3_pump = value.split(',')
				self.ch2_stage3_pump_Display.SetLabel(str(self.ch2_stage3_pump))
			if parameter == 'ch2_stage3_drain':
				self.ch2_stage3_drain = value.split(',')
				self.ch2_stage3_drain_Display.SetLabel(str(self.ch2_stage3_drain))
			if parameter == 'tank_size':
				self.tankSize = int(value)
				self.tankSize_Display.SetLabel(str(self.tankSize))
			if parameter == 'water_check':
				self.waterCheckTiming = value.split(',')
				self.waterCheck_Display.SetLabel(str(self.waterCheckTiming))
			if parameter == 'ec_check':
				self.ecCheckTiming = value.split(',')
				self.ecCheck_Display.SetLabel(str(self.ecCheckTiming))
			if parameter == 'stage1_ec':
				self.stage1Ec = float(value)
				self.stage1Ec_Display.SetLabel(str(self.stage1Ec))
			if parameter == 'stage2_ec':
				self.stage2Ec = float(value)
				self.stage2Ec_Display.SetLabel(str(self.stage2Ec))
			if parameter == 'stage3_ec':
				self.stage3Ec = float(value)
				self.stage3Ec_Display.SetLabel(str(self.stage3Ec))
			if parameter == 'ch1_stage1_duration':
				self.ch1_stage1_duration = int(value)
				self.ch1_stage1_duration_Display.SetLabel(str(self.ch1_stage1_duration))
			if parameter == 'ch1_stage2_duration':
				self.ch1_stage2_duration = int(value)
				self.ch1_stage2_duration_Display.SetLabel(str(self.ch1_stage2_duration))
			if parameter == 'ch1_stage3_duration':
				self.ch1_stage3_duration = int(value)
				self.ch1_stage3_duration_Display.SetLabel(str(self.ch1_stage3_duration))
			if parameter == 'ch2_stage1_duration':
				self.ch2_stage1_duration = int(value)
				self.ch2_stage1_duration_Display.SetLabel(str(self.ch2_stage1_duration))
			if parameter == 'ch2_stage2_duration':
				self.ch2_stage2_duration = int(value)
				self.ch2_stage2_duration_Display.SetLabel(str(self.ch2_stage2_duration))
			if parameter == 'ch2_stage3_duration':
				self.ch2_stage3_duration = int(value)
				self.ch2_stage3_duration_Display.SetLabel(str(self.ch2_stage3_duration))

			if parameter == 'dwcLight_stage1_power':
				self.dwcLight_stage1_power = int(value)
				self.dwcLight_stage1_power_Display.SetLabel(str(self.dwcLight_stage1_power))
			if parameter == 'dwcLight_stage1_distance':
				self.dwcLight_stage1_distance = int(value)
				self.dwcLight_stage1_distance_Display.SetLabel(str(self.dwcLight_stage1_distance))
			if parameter == 'dwcLight_stage1_on':
				self.dwcLight_stage1_on = value.split(',')
				self.dwcLight_stage1_on_Display.SetLabel(str(self.dwcLight_stage1_on))
			if parameter == 'dwcLight_stage1_off':
				self.dwcLight_stage1_off = value.split(',')
				self.dwcLight_stage1_off_Display.SetLabel(str(self.dwcLight_stage1_off))
			if parameter == 'dwcLight_stage1_duration':
				self.dwcLight_stage1_duration = int(value)
				self.dwcLight_stage1_duration_Display.SetLabel(str(self.dwcLight_stage1_duration))

			if parameter == 'dwcLight_stage2_power':
				self.dwcLight_stage2_power = int(value)
				self.dwcLight_stage2_power_Display.SetLabel(str(self.dwcLight_stage2_power))
			if parameter == 'dwcLight_stage2_distance':
				self.dwcLight_stage2_distance = int(value)
				self.dwcLight_stage2_distance_Display.SetLabel(str(self.dwcLight_stage2_distance))
			if parameter == 'dwcLight_stage2_on':
				self.dwcLight_stage2_on = value.split(',')
				self.dwcLight_stage2_on_Display.SetLabel(str(self.dwcLight_stage2_on))
			if parameter == 'dwcLight_stage2_off':
				self.dwcLight_stage2_off = value.split(',')
				self.dwcLight_stage2_off_Display.SetLabel(str(self.dwcLight_stage2_off))
			if parameter == 'dwcLight_stage2_duration':
				self.dwcLight_stage2_duration = int(value)
				self.dwcLight_stage2_duration_Display.SetLabel(str(self.dwcLight_stage2_duration))

			if parameter == 'dwcLight_stage3_power':
				self.dwcLight_stage3_power = int(value)
				self.dwcLight_stage3_power_Display.SetLabel(str(self.dwcLight_stage3_power))
			if parameter == 'dwcLight_stage3_distance':
				self.dwcLight_stage3_distance = int(value)
				self.dwcLight_stage3_distance_Display.SetLabel(str(self.dwcLight_stage3_distance))
			if parameter == 'dwcLight_stage3_on':
				self.dwcLight_stage3_on = value.split(',')
				self.dwcLight_stage3_on_Display.SetLabel(str(self.dwcLight_stage3_on))
			if parameter == 'dwcLight_stage3_off':
				self.dwcLight_stage3_off = value.split(',')
				self.dwcLight_stage3_off_Display.SetLabel(str(self.dwcLight_stage3_off))
			if parameter == 'dwcLight_stage3_duration':
				self.dwcLight_stage3_duration = int(value)
				self.dwcLight_stage3_duration_Display.SetLabel(str(self.dwcLight_stage3_duration))

			if parameter == 'dwcTopup_frequency':
				self.dwcTopup_frequency = int(value)
				self.dwcTopup_frequency_Display.SetLabel(str(self.dwcTopup_frequency))
			if parameter == 'dwcTopup_timing':
				self.dwcTopup_timing = value.split(',')
				self.dwcTopup_timing_Display.SetLabel(str(self.dwcTopup_timing))

	def LoadLog(self,event):
		with wx.FileDialog(self, "Open Text file", wildcard="Text files (*.txt)|*.txt",\
			style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			self.logFile = fileDialog.GetPath()
			logFileSplit = self.logFile.split('/') #split the path
			self.log_Display.SetLabel(logFileSplit[-1]) # only display the file name from the path

	def DoserCheck(self):
		if self.autoDoser_ToggleBtn.GetValue() == True:
			for thisTime in self.waterCheckTiming:
				if thisTime == self.timeNow:
					self.DoserPumpFunction(1)
			for thisTime in self.ecCheckTiming:
				if thisTime == self.timeNow:
					self.EcDoseFunction()

	def PublishToCommandTopic(self,message):
		publish.single(self.commandTopic,message,hostname=self.host)

	def DoserPumpFunction(self,state):
		self.PublishToCommandTopic('PU {}'.format(state))
	
	def EcDoseFunction(self):
		self.PublishToCommandTopic('AEC 1')

	def EcDose(self,ecValue):
		nutrientVolume = 0
		EcFactor = 100.0
		if ecValue == 0 or ecValue == 100:
			nutrientVolume = 0
		elif self.ch1CurrentStage == 1:
			nutrientVolume = (self.stage1Ec - ecValue) * float(self.tankSize / EcFactor)
		elif self.ch1CurrentStage == 2:
			nutrientVolume = (self.stage2Ec - ecValue) * float(self.tankSize / EcFactor)
		elif self.ch1CurrentStage == 3:
			nutrientVolume = (self.stage3Ec - ecValue) * float(self.tankSize / EcFactor)
		nutrientVolume = int(round(nutrientVolume))
		if nutrientVolume <= 0:
			pass
		else:
			self.PublishToCommandTopic('NP {}'.format(nutrientVolume/2))

	def LightCheck(self):
		if self.autoLight1_ToggleBtn.GetValue() == True:
			if self.ch1CurrentStage == 1:
				for thisTime in self.light1_stage1_on:
					if thisTime == self.timeNow:
						self.LightFunction(1,1)
				for thisTime in self.light1_stage1_off:
					if thisTime == self.timeNow:
						self.LightFunction(1,0)
			elif self.ch1CurrentStage == 2:
				for thisTime in self.light1_stage2_on:
					if thisTime == self.timeNow:
						self.LightFunction(1,1)
				for thisTime in self.light1_stage2_off:
					if thisTime == self.timeNow:
						self.LightFunction(1,0)
			elif self.ch1CurrentStage == 3:
				for thisTime in self.light1_stage3_on:
					if thisTime == self.timeNow:
						self.LightFunction(1,1)
				for thisTime in self.light1_stage3_off:
					if thisTime == self.timeNow:
						self.LightFunction(1,0)

		if self.autoLight2_ToggleBtn.GetValue() == True:
			if self.ch2CurrentStage == 1:
				for thisTime in self.light2_stage1_on:
					if thisTime == self.timeNow:
						self.LightFunction(2,1)
				for thisTime in self.light2_stage1_off:
					if thisTime == self.timeNow:
						self.LightFunction(2,0)
			elif self.ch2CurrentStage == 2:
				for thisTime in self.light2_stage2_on:
					if thisTime == self.timeNow:
						self.LightFunction(2,1)
				for thisTime in self.light2_stage2_off:
					if thisTime == self.timeNow:
						self.LightFunction(2,0)
			elif self.ch2CurrentStage == 3:
				for thisTime in self.light2_stage3_on:
					if thisTime == self.timeNow:
						self.LightFunction(2,1)
				for thisTime in self.light2_stage3_off:
					if thisTime == self.timeNow:
						self.LightFunction(2,0)

		'''  DWC light '''
		if self.dwcAuto_ToggleBtn.GetValue() == True:
			if self.dwcLightCurrentStage == 1:
				for thisTime in self.dwcLight_stage1_on:
					if thisTime == self.timeNow:
						self.DwcLightFunction(1,self.dwcLight_stage1_power,self.dwcLight_stage1_distance)
						self.DwcLightFunction(2,self.dwcLight_stage1_power,self.dwcLight_stage1_distance)

	def DwcLightFunction(self,light,power,distance):
		self.PublishToCommandTopic('LP{} {}'.format(light,power))
		self.PublishToCommandTopic('LD{} {}'.format(light,distance))

	def IrrigationCheck(self):
		if self.autoPump1_ToggleBtn.GetValue() == True:
			if self.ch1CurrentStage == 1:
				for thisTime in self.ch1_stage1_pump:
					if thisTime == self.timeNow:
						self.PumpFunction(1,1)
				for thisTime in self.ch1_stage1_drain:
					if thisTime == self.timeNow:
						self.DrainFunction(1,1)
			elif self.ch1CurrentStage == 2:
				for thisTime in self.ch1_stage2_pump:
					if thisTime == self.timeNow:
						self.self.PumpFunction(1,1)
				for thisTime in self.ch1_stage2_drain:
					if thisTime == self.timeNow:
						self.DrainFunction(1,1)
			elif self.ch1CurrentStage == 3:
				for thisTime in self.ch1_stage3_pump:
					if thisTime == self.timeNow:
						self.PumpFunction(1,1)
				for thisTime in self.ch1_stage3_drain:
					if thisTime == self.timeNow:
						self.DrainFunction(1,1)
		if self.autoPump2_ToggleBtn.GetValue() == True:
			if self.ch2CurrentStage == 1:
				for thisTime in self.ch2_stage1_pump:
					if thisTime == self.timeNow:
						self.PumpFunction(2,1)
				for thisTime in self.ch2_stage1_drain:
					if thisTime == self.timeNow:
						self.DrainFunction(2,1)
			if self.ch2CurrentStage == 2:
				for thisTime in self.ch2_stage2_pump:
					if thisTime == self.timeNow:
						self.PumpFunction(2,1)
				for thisTime in self.ch2_stage2_drain:
					if thisTime == self.timeNow:
						self.DrainFunction(2,1)
			if self.ch2CurrentStage == 3:
				for thisTime in self.ch2_stage3_pump:
					if thisTime == self.timeNow:
						self.PumpFunction(2,1)
				for thisTime in self.ch2_stage3_drain:
					if thisTime == self.timeNow:
						self.DrainFunction(2,1)

	def LightFunction(self,light,state):
		self.PublishToCommandTopic('LT{} {}'.format(light,state))

	def PumpFunction(self,pump,state):
		self.PublishToCommandTopic('PU{} {}'.format(pump,state))

	def DrainFunction(self,drain,state):
		self.PublishToCommandTopic('DR{} {}'.format(drain,state))

	def CheckIrrigation1Fields(self,event):
		if not self.ch1_stage1_pump:
			print ('unable to AUTO')
			self.autoPump1_ToggleBtn.SetValue(False)

	def CheckIrrigation2Fields(self,event):
		if not self.ch2_stage1_pump:
			print ('unable to AUTO')
			self.autoPump2_ToggleBtn.SetValue(False)

	def CheckDoserFields(self,event):
		if not self.waterCheckTiming:
			print('unable to AUTO')
			self.autoDoser_ToggleBtn.SetValue(False)

	def CheckLight1Fields(self,event):
		if not self.light1_stage1_on:
			print('unable to AUTO')
			self.autoLight1_ToggleBtn.SetValue(False)

	def CheckLight2Fields(self,event):
		if not self.light2_stage1_on:
			print('unable to AUTO')
			self.autoLight2_ToggleBtn.SetValue(False)

	def CheckMQTTMessage(self,dataType,dataValue):
		if dataType == 'TP1' or dataType == 'TP2':
			self.ShowTemperature(dataType,dataValue)
		elif dataType == 'HM1':
			self.ShowHumidity(dataValue)
		elif dataType == 'EC':
			self.ec = dataValue
		elif dataType == 'AEC':
			self.ec = dataValue
			self.EcDose(self.ec)

	def UpdateSensors(self):
		self.ec_Display.SetLabel(str(self.ec))

	def ShowTemperature(self,sensor,temperature):
		if sensor == 'TP1':
			self.temp1 = temperature
			self.temp1_Display.SetLabel(str(self.temp1))
		elif sensor == 'TP2':
			self.temp2 = temperature
			self.temp2_Display.SetLabel(str(self.temp2))
		tempA = round (((self.temp1 + self.temp2)/2),2)
		self.tempA_Display.SetLabel(str(tempA))

	def ShowHumidity(self,humidity):
		self.humidity = humidity
		self.humidity_Display.SetLabel(self.humidity)

def main():
	app = wx.App(False)
	frame = Irrigation(None)
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	main()
