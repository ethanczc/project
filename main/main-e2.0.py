import wx
import gui_main_e2_0 as gui
import time
import datetime
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
'''
new version from 1.0
Now uses MQTT to issue commands to a command topic 'RACK1'
and listens to sensors topic 'RACK1S'
Merge all systems into 1 uniform staged system and 3 modules, irrigation(4 ch), LED(4 ch), and doser
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

		self.stage1Fill, self.stage1Drain = [], []
		self.stage2Fill, self.stage2Drain = [], []
		self.stage3Fill, self.stage3Drain = [], []

		self.stage1LedOn, self.stage1LedOff = [], []
		self.stage2LedOn, self.stage2LedOff = [], []
		self.stage3LedOn, self.stage3LedOff = [], []

		self.stage1LedPwr, self.stage1LedDist= 0, 0
		self.stage2LedPwr, self.stage2LedDist= 0, 0
		self.stage3LedPwr, self.stage3LedDist= 0, 0

		self.stage1Ec, self.stage2Ec, self.stage3Ec = 0, 0, 0
		self.stage1Topup, self.stage1Dose = [], []
		self.stage2Topup, self.stage2Dose = [], []
		self.stage3Topup, self.stage3Dose = [], []

		self.currentStage = 0
		self.stage1Duration, self.stage2Duration, self.stage3Duration = 0, 0, 0
		self.ec = 0.0
		self.tankSize = 6000

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
		dataType = message[0]
		dataValue = float(message[1])
		self.CheckMQTTMessage(dataType,dataValue)

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
			if daysPassed <= self.currentStage:
				self.currentStage = 1
			elif self.stage1Duration <= daysPassed <= (self.stage1Duration + self.stage2Duration):
				self.currentStage = 2
			elif (self.stage1Duration + self.stage2Duration) <= daysPassed <= (self.stage1Duration + self.stage2Duration\
			+ self.stage3Duration):
				self.currentStage = 3
			else:
				self.currentStage = 3
			self.currentStage_Display.SetLabel(str(self.currentStage))

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
			if parameter == 'stage1_fill':
				self.stage1Fill = value.split(',')
				self.stage1Fill_Display.SetLabel(str(self.stage1Fill))
			if parameter == 'stage1_drain':
				self.stage1Drain = value.split(',')
				self.stage1Drain_Display.SetLabel(str(self.stage1Drain))
			if parameter == 'stage2_fill':
				self.stage2Fill = value.split(',')
				self.stage2Fill_Display.SetLabel(str(self.stage2Fill))
			if parameter == 'stage2_drain':
				self.stage2Drain = value.split(',')
				self.stage2Drain_Display.SetLabel(str(self.stage2Drain))
			if parameter == 'stage3_fill':
				self.stage3Fill = value.split(',')
				self.stage3Fill_Display.SetLabel(str(self.stage3Fill))
			if parameter == 'stage3_drain':
				self.stage3Drain = value.split(',')
				self.stage3Drain_Display.SetLabel(str(self.stage3Drain))
			if parameter == 'stage1_led_on':
				self.stage1LedOn = value.split(',')
				self.stage1LedOn_Display.SetLabel(str(self.stage1LedOn))
			if parameter == 'stage1_led_off':
				self.stage1LedOff = value.split(',')
				self.stage1LedOff_Display.SetLabel(str(self.stage1LedOff))
			if parameter == 'stage1_led_pwr':
				self.stage1LedPwr = int(value)
				self.stage1LedPwr_Display.SetLabel(str(self.stage1LedPwr))
			if parameter == 'stage1_led_dist':
				self.stage1LedDist = int(value)
				self.stage1LedDist_Display.SetLabel(str(self.stage1LedDist))
			if parameter == 'stage2_led_on':
				self.stage2LedOn = value.split(',')
				self.stage2LedOn_Display.SetLabel(str(self.stage2LedOn))
			if parameter == 'stage2_led_off':
				self.stage2LedOff = value.split(',')
				self.stage2LedOff_Display.SetLabel(str(self.stage2LedOff))
			if parameter == 'stage2_led_pwr':
				self.stage2LedPwr = int(value)
				self.stage2LedPwr_Display.SetLabel(str(self.stage2LedPwr))
			if parameter == 'stage2_led_dist':
				self.stage2LedDist = int(value)
				self.stage2LedDist_Display.SetLabel(str(self.stage2LedDist))
			if parameter == 'stage3_led_on':
				self.stage3LedOn = value.split(',')
				self.stage3LedOn_Display.SetLabel(str(self.stage3LedOn))
			if parameter == 'stage3_led_off':
				self.stage3LedOff = value.split(',')
				self.stage3LedOff_Display.SetLabel(str(self.stage3LedOff))
			if parameter == 'stage3_led_pwr':
				self.stage3LedPwr = int(value)
				self.stage3LedPwr_Display.SetLabel(str(self.stage3LedPwr))
			if parameter == 'stage3_led_dist':
				self.stage3LedDist = int(value)
				self.stage3LedDist_Display.SetLabel(str(self.stage3LedDist))
			if parameter == 'stage1_ec':
				self.stage1Ec = float(value)
				self.stage1Ec_Display.SetLabel(str(self.stage1Ec))
			if parameter == 'stage1_topup':
				self.stage1Topup = value.split(',')
				self.stage1Topup_Display.SetLabel(str(self.stage1Topup))
			if parameter == 'stage1_dose':
				self.stage1Dose = value.split(',')
				self.stage1Dose_Display.SetLabel(str(self.stage1Dose))
			if parameter == 'stage2_ec':
				self.stage2Ec = float(value)
				self.stage2Ec_Display.SetLabel(str(self.stage2Ec))
			if parameter == 'stage2_topup':
				self.stage2Topup = value.split(',')
				self.stage2Topup_Display.SetLabel(str(self.stage2Topup))
			if parameter == 'stage2_dose':
				self.stage2Dose = value.split(',')
				self.stage2Dose_Display.SetLabel(str(self.stage2Dose))
			if parameter == 'stage3_ec':
				self.stage3Ec = float(value)
				self.stage3Ec_Display.SetLabel(str(self.stage3Ec))
			if parameter == 'stage3_topup':
				self.stage3Topup = value.split(',')
				self.stage3Topup_Display.SetLabel(str(self.stage3Topup))
			if parameter == 'stage3_dose':
				self.stage3Dose = value.split(',')
				self.stage3Dose_Display.SetLabel(str(self.stage3Dose))
			if parameter == 'stage1_duration':
				self.stage1Duration = int(value)
				self.stage1Duration_Display.SetLabel(str(self.stage1Duration))
			if parameter == 'stage2_duration':
				self.stage2Duration = int(value)
				self.stage2Duration_Display.SetLabel(str(self.stage2Duration))
			if parameter == 'stage3_duration':
				self.stage3Duration = int(value)
				self.stage3Duration_Display.SetLabel(str(self.stage3Duration))

	def LoadLog(self,event):
		with wx.FileDialog(self, "Open Text file", wildcard="Text files (*.txt)|*.txt",\
			style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			self.logFile = fileDialog.GetPath()
			logFileSplit = self.logFile.split('/') #split the path
			self.log_Display.SetLabel(logFileSplit[-1]) # only display the file name from the path

	def DoserCheck(self):
		if self.doser_ToggleBtn.GetValue() == True:
			if self.currentStage == 1:
				for thisTime in self.stage1Topup:
					if thisTime == self.timeNow:
						self.TopupFunction(1)
				for thisTime in self.stage1Dose:
					if thisTime == self.timeNow:
						self.EcDoseFunction()
			elif self.currentStage == 2:
				for thisTime in self.stage2Topup:
					if thisTime == self.timeNow:
						self.TopupFunction(1)
				for thisTime in self.stage2Dose:
					if thisTime == self.timeNow:
						self.EcDoseFunction()
			elif self.currentStage == 3:
				for thisTime in self.stage3Topup:
					if thisTime == self.timeNow:
						self.TopupFunction(1)
				for thisTime in self.stage3Dose:
					if thisTime == self.timeNow:
						self.EcDoseFunction()
			
	def PublishToCommandTopic(self,message):
		publish.single(self.commandTopic,message,hostname=self.host)

	def TopupFunction(self,state):
		self.PublishToCommandTopic('PU {}'.format(state))
	
	def EcDoseFunction(self):
		self.PublishToCommandTopic('AEC 1')

	def EcDose(self,ecValue):
		nutrientVolume = 0
		EcFactor = 100.0
		if ecValue == 0 or ecValue == 100:
			nutrientVolume = 0
		elif self.currentStage == 1:
			nutrientVolume = (self.stage1Ec - ecValue) * float(self.tankSize / EcFactor)
		elif self.currentStage == 2:
			nutrientVolume = (self.stage2Ec - ecValue) * float(self.tankSize / EcFactor)
		elif self.currentStage == 3:
			nutrientVolume = (self.stage3Ec - ecValue) * float(self.tankSize / EcFactor)
		nutrientVolume = int(round(nutrientVolume))
		if nutrientVolume <= 0:
			pass
		else:
			self.PublishToCommandTopic('NP {}'.format(nutrientVolume/2))

	def LightCheck(self):
		if self.led_ToggleBtn.GetValue() == True:
			if self.currentStage == 1:
				for thisTime in self.stage1LedOn:
					if thisTime == self.timeNow:
						#self.LightPwrFunction(0,self.stage1LedPwr)
						self.LightDistFunction(0,self.stage1LedDist)
				for thisTime in self.stage1LedOff:
					if thisTime == self.timeNow:
						self.LightPwrFunction(0,0)
			elif self.currentStage == 2:
				for thisTime in self.stage2LedOn:
					if thisTime == self.timeNow:
						self.LightPwrFunction(0,self.stage2LedPwr)
						self.LightDistFunction(0,self.stage2LedDist)
				for thisTime in self.stage2LedOff:
					if thisTime == self.timeNow:
						self.LightPwrFunction(0,0)
			elif self.currentStage == 3:
				for thisTime in self.stage3LedOn:
					if thisTime == self.timeNow:
						self.LightPwrFunction(0,self.stage3LedPwr)
						self.LightDistFunction(0,self.stage3LedDist)
				for thisTime in self.stage3LedOff:
					if thisTime == self.timeNow:
						self.LightPwrFunction(0,0)

	def IrrigationCheck(self):
		if self.irrigation_ToggleBtn.GetValue() == True:
			if self.currentStage == 1:
				for thisTime in self.stage1Fill:
					if thisTime == self.timeNow:
						self.PumpFunction(1,1)
				for thisTime in self.stage1Drain:
					if thisTime == self.timeNow:
						self.DrainFunction(1,1)
			elif self.currentStage == 2:
				for thisTime in self.stage2Fill:
					if thisTime == self.timeNow:
						self.self.PumpFunction(1,1)
				for thisTime in self.stage2Drain:
					if thisTime == self.timeNow:
						self.DrainFunction(1,1)
			elif self.currentStage == 3:
				for thisTime in self.stage3Fill:
					if thisTime == self.timeNow:
						self.PumpFunction(1,1)
				for thisTime in self.stage3Drain:
					if thisTime == self.timeNow:
						self.DrainFunction(1,1)

	def LightPwrFunction(self,light,power):
		self.PublishToCommandTopic('LP{} {}'.format(light,power))

	def LightDistFunction(self,light,distance):
		self.PublishToCommandTopic('LD{} {}'.format(light,distance))

	def PumpFunction(self,pump,state):
		self.PublishToCommandTopic('PU{} {}'.format(pump,state))

	def DrainFunction(self,drain,state):
		self.PublishToCommandTopic('DR{} {}'.format(drain,state))

	def CheckIrrigationFields(self,event):
		if not self.stage1Fill:
			print ('unable to AUTO')
			self.irrigation_ToggleBtn.SetValue(False)

	def CheckDoserFields(self,event):
		if not self.stage1Topup:
			print('unable to AUTO')
			self.doser_ToggleBtn.SetValue(False)

	def CheckLedFields(self,event):
		if not self.stage1LedOn:
			print('unable to AUTO')
			self.led_ToggleBtn.SetValue(False)

	def CheckMQTTMessage(self,dataType,dataValue):
		if dataType == 'EC':
			self.ec = dataValue
			print (self.ec)
		elif dataType == 'AEC':
			self.ec = dataValue
			self.EcDose(self.ec)

	def UpdateSensors(self):
		self.ec_Display.SetLabel(str(self.ec))

def main():
	app = wx.App(False)
	frame = Irrigation(None)
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	main()
