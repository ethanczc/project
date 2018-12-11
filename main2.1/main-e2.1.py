import wx
import gui_main_e2_1 as gui
import time
import datetime
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
'''
new version from 2.0
system is 2 channel system, but able to stick to 1 uniform channel to issue LP0, LD0, PU0 commands

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

		''' channel 1 '''

		self.stage1Fill1, self.stage1Drain1 = [], []
		self.stage2Fill1, self.stage2Drain1 = [], []
		self.stage3Fill1, self.stage3Drain1 = [], []

		self.stage1Led1On, self.stage1Led1Off = [], []
		self.stage2Led1On, self.stage2Led1Off = [], []
		self.stage3Led1On, self.stage3Led1Off = [], []

		self.stage1Led1Pwr, self.stage1Led1Dist= 0, 0
		self.stage2Led1Pwr, self.stage2Led1Dist= 0, 0
		self.stage3Led1Pwr, self.stage3Led1Dist= 0, 0

		''' channel 2 '''

		self.stage1Fill2, self.stage1Drain2 = [], []
		self.stage2Fill2, self.stage2Drain2 = [], []
		self.stage3Fill2, self.stage3Drain2 = [], []

		self.stage1Led2On, self.stage1Led2Off = [], []
		self.stage2Led2On, self.stage2Led2Off = [], []
		self.stage3Led2On, self.stage3Led2Off = [], []

		self.stage1Led2Pwr, self.stage1Led2Dist= 0, 0
		self.stage2Led2Pwr, self.stage2Led2Dist= 0, 0
		self.stage3Led2Pwr, self.stage3Led2Dist= 0, 0

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
		self.IrrigationCheck1()
		self.LightCheck1()
		self.IrrigationCheck2()
		self.LightCheck2()
		self.DoserCheck()
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
				'''channel 1'''
			if parameter == 'stage1_fill1':
				self.stage1Fill1 = value.split(',')
				self.stage1Fill1_Display.SetLabel(str(self.stage1Fill1))
			if parameter == 'stage1_drain1':
				self.stage1Drain1 = value.split(',')
				self.stage1Drain1_Display.SetLabel(str(self.stage1Drain1))
			if parameter == 'stage2_fill1':
				self.stage2Fill1 = value.split(',')
				self.stage2Fill1_Display.SetLabel(str(self.stage2Fill1))
			if parameter == 'stage2_drain1':
				self.stage2Drain1 = value.split(',')
				self.stage2Drain1_Display.SetLabel(str(self.stage2Drain1))
			if parameter == 'stage3_fill1':
				self.stage3Fill1 = value.split(',')
				self.stage3Fill1_Display.SetLabel(str(self.stage3Fill1))
			if parameter == 'stage3_drain1':
				self.stage3Drain1 = value.split(',')
				self.stage3Drain1_Display.SetLabel(str(self.stage3Drain1))
			if parameter == 'stage1_led1_on':
				self.stage1Led1On = value.split(',')
				self.stage1Led1On_Display.SetLabel(str(self.stage1Led1On))
			if parameter == 'stage1_led1_off':
				self.stage1Led1Off = value.split(',')
				self.stage1Led1Off_Display.SetLabel(str(self.stage1Led1Off))
			if parameter == 'stage1_led1_pwr':
				self.stage1Led1Pwr = int(value)
				self.stage1Led1Pwr_Display.SetLabel(str(self.stage1Led1Pwr))
			if parameter == 'stage1_led1_dist':
				self.stage1Led1Dist = int(value)
				self.stage1Led1Dist_Display.SetLabel(str(self.stage1Led1Dist))
			if parameter == 'stage2_led1_on':
				self.stage2Led1On = value.split(',')
				self.stage2Led1On_Display.SetLabel(str(self.stage2Led1On))
			if parameter == 'stage2_led1_off':
				self.stage2Led1Off = value.split(',')
				self.stage2Led1Off_Display.SetLabel(str(self.stage2Led1Off))
			if parameter == 'stage2_led1_pwr':
				self.stage2Led1Pwr = int(value)
				self.stage2Led1Pwr_Display.SetLabel(str(self.stage2Led1Pwr))
			if parameter == 'stage2_led1_dist':
				self.stage2Led1Dist = int(value)
				self.stage2Led1Dist_Display.SetLabel(str(self.stage2Led1Dist))
			if parameter == 'stage3_led1_on':
				self.stage3Led1On = value.split(',')
				self.stage3Led1On_Display.SetLabel(str(self.stage3Led1On))
			if parameter == 'stage3_led1_off':
				self.stage3Led1Off = value.split(',')
				self.stage3Led1Off_Display.SetLabel(str(self.stage3Led1Off))
			if parameter == 'stage3_led1_pwr':
				self.stage3Led1Pwr = int(value)
				self.stage3Led1Pwr_Display.SetLabel(str(self.stage3Led1Pwr))
			if parameter == 'stage3_led1_dist':
				self.stage3Led1Dist = int(value)
				self.stage3Led1Dist_Display.SetLabel(str(self.stage3Led1Dist))
				'''channel 2'''
			if parameter == 'stage1_fill2':
				self.stage1Fill2 = value.split(',')
				self.stage1Fill2_Display.SetLabel(str(self.stage1Fill2))
			if parameter == 'stage1_drain2':
				self.stage1Drain2 = value.split(',')
				self.stage1Drain2_Display.SetLabel(str(self.stage1Drain2))
			if parameter == 'stage2_fill2':
				self.stage2Fill2 = value.split(',')
				self.stage2Fill2_Display.SetLabel(str(self.stage2Fill2))
			if parameter == 'stage2_drain2':
				self.stage2Drain2 = value.split(',')
				self.stage2Drain2_Display.SetLabel(str(self.stage2Drain2))
			if parameter == 'stage3_fill2':
				self.stage3Fill2 = value.split(',')
				self.stage3Fill2_Display.SetLabel(str(self.stage3Fill2))
			if parameter == 'stage3_drain2':
				self.stage3Drain2 = value.split(',')
				self.stage3Drain2_Display.SetLabel(str(self.stage3Drain2))
			if parameter == 'stage1_led2_on':
				self.stage1Led2On = value.split(',')
				self.stage1Led2On_Display.SetLabel(str(self.stage1Led2On))
			if parameter == 'stage1_led2_off':
				self.stage1Led2Off = value.split(',')
				self.stage1Led2Off_Display.SetLabel(str(self.stage1Led2Off))
			if parameter == 'stage1_led2_pwr':
				self.stage1Led2Pwr = int(value)
				self.stage1Led2Pwr_Display.SetLabel(str(self.stage1Led2Pwr))
			if parameter == 'stage1_led2_dist':
				self.stage1Led2Dist = int(value)
				self.stage1Led2Dist_Display.SetLabel(str(self.stage1Led2Dist))
			if parameter == 'stage2_led2_on':
				self.stage2Led2On = value.split(',')
				self.stage2Led2On_Display.SetLabel(str(self.stage2Led2On))
			if parameter == 'stage2_led2_off':
				self.stage2Led2Off = value.split(',')
				self.stage2Led2Off_Display.SetLabel(str(self.stage2Led2Off))
			if parameter == 'stage2_led2_pwr':
				self.stage2Led2Pwr = int(value)
				self.stage2Led2Pwr_Display.SetLabel(str(self.stage2Led2Pwr))
			if parameter == 'stage2_led2_dist':
				self.stage2Led2Dist = int(value)
				self.stage2Led2Dist_Display.SetLabel(str(self.stage2Led2Dist))
			if parameter == 'stage3_led2_on':
				self.stage3Led2On = value.split(',')
				self.stage3Led2On_Display.SetLabel(str(self.stage3Led2On))
			if parameter == 'stage3_led2_off':
				self.stage3Led2Off = value.split(',')
				self.stage3Led2Off_Display.SetLabel(str(self.stage3Led2Off))
			if parameter == 'stage3_led2_pwr':
				self.stage3Led2Pwr = int(value)
				self.stage3Led2Pwr_Display.SetLabel(str(self.stage3Led2Pwr))
			if parameter == 'stage3_led2_dist':
				self.stage3Led2Dist = int(value)
				self.stage3Led2Dist_Display.SetLabel(str(self.stage3Led2Dist))

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

	def LightCheck1(self):
		channel = 1
		if self.singleChannelMode_CheckBox.GetValue() == True:
			channel = 0
		if self.led1_ToggleBtn.GetValue() == True:
			if self.currentStage == 1:
				for thisTime in self.stage1Led1On:
					if thisTime == self.timeNow:
						self.LightPwrFunction(channel,self.stage1Led1Pwr)
						time.sleep(2)
						self.LightDistFunction(channel,self.stage1Led1Dist)
				for thisTime in self.stage1Led1Off:
					if thisTime == self.timeNow:
						self.LightPwrFunction(channel,0)
			elif self.currentStage == 2:
				for thisTime in self.stage2Led1On:
					if thisTime == self.timeNow:
						self.LightPwrFunction(channel,self.stage2Led1Pwr)
						time.sleep(2)
						self.LightDistFunction(channel,self.stage2Led1Dist)
				for thisTime in self.stage2Led1Off:
					if thisTime == self.timeNow:
						self.LightPwrFunction(channel,0)
			elif self.currentStage == 3:
				for thisTime in self.stage3Led1On:
					if thisTime == self.timeNow:
						self.LightPwrFunction(channel,self.stage3Led1Pwr)
						time.sleep(2)
						self.LightDistFunction(channel,self.stage3Led1Dist)
				for thisTime in self.stage3Led1Off:
					if thisTime == self.timeNow:
						self.LightPwrFunction(channel,0)

	def LightCheck2(self):
		if self.led2_ToggleBtn.GetValue() == True:
			if self.currentStage == 1:
				for thisTime in self.stage1Led2On:
					if thisTime == self.timeNow:
						self.LightPwrFunction(2,self.stage1Led2Pwr)
						time.sleep(2)
						self.LightDistFunction(2,self.stage1Led2Dist)
				for thisTime in self.stage1Led2Off:
					if thisTime == self.timeNow:
						self.LightPwrFunction(2,0)
			elif self.currentStage == 2:
				for thisTime in self.stage2Led2On:
					if thisTime == self.timeNow:
						self.LightPwrFunction(2,self.stage2Led2Pwr)
						time.sleep(2)
						self.LightDistFunction(2,self.stage2Led2Dist)
				for thisTime in self.stage2Led2Off:
					if thisTime == self.timeNow:
						self.LightPwrFunction(2,0)
			elif self.currentStage == 3:
				for thisTime in self.stage3Led2On:
					if thisTime == self.timeNow:
						self.LightPwrFunction(2,self.stage3Led2Pwr)
						time.sleep(2)
						self.LightDistFunction(2,self.stage3Led2Dist)
				for thisTime in self.stage3Led2Off:
					if thisTime == self.timeNow:
						self.LightPwrFunction(2,0)

	def IrrigationCheck1(self):
		channel = 1
		if self.singleChannelMode_CheckBox.GetValue() == True:
			channel = 0
		if self.irrigation1_ToggleBtn.GetValue() == True:
			if self.currentStage == 1:
				for thisTime in self.stage1Fill1:
					if thisTime == self.timeNow:
						self.PumpFunction(channel,1)
				for thisTime in self.stage1Drain1:
					if thisTime == self.timeNow:
						self.DrainFunction(channel,1)
			elif self.currentStage == 2:
				for thisTime in self.stage2Fill1:
					if thisTime == self.timeNow:
						self.PumpFunction(channel,1)
				for thisTime in self.stage2Drain1:
					if thisTime == self.timeNow:
						self.DrainFunction(channel,1)
			elif self.currentStage == 3:
				for thisTime in self.stage3Fill1:
					if thisTime == self.timeNow:
						self.PumpFunction(channel,1)
				for thisTime in self.stage3Drain1:
					if thisTime == self.timeNow:
						self.DrainFunction(channel,1)

	def IrrigationCheck2(self):
		if self.irrigation2_ToggleBtn.GetValue() == True:
			if self.currentStage == 1:
				for thisTime in self.stage1Fill2:
					if thisTime == self.timeNow:
						self.PumpFunction(2,1)
				for thisTime in self.stage1Drain2:
					if thisTime == self.timeNow:
						self.DrainFunction(2,1)
			elif self.currentStage == 2:
				for thisTime in self.stage2Fill2:
					if thisTime == self.timeNow:
						self.PumpFunction(2,1)
				for thisTime in self.stage2Drain2:
					if thisTime == self.timeNow:
						self.DrainFunction(2,1)
			elif self.currentStage == 3:
				for thisTime in self.stage3Fill2:
					if thisTime == self.timeNow:
						self.PumpFunction(2,1)
				for thisTime in self.stage3Drain2:
					if thisTime == self.timeNow:
						self.DrainFunction(2,1)

	def LightPwrFunction(self,light,power):
		self.PublishToCommandTopic('LP{} {}'.format(light,power))

	def LightDistFunction(self,light,distance):
		self.PublishToCommandTopic('LD{} {}'.format(light,distance))

	def PumpFunction(self,pump,state):
		self.PublishToCommandTopic('PU{} {}'.format(pump,state))

	def DrainFunction(self,drain,state):
		self.PublishToCommandTopic('DR{} {}'.format(drain,state))

	def ActivateSingleChannel(self,event):
		'''when single channel mode check box is ticked, disable auto for
		irrigation2 and led2 '''
		if self.singleChannelMode_CheckBox.GetValue() == True:
			self.irrigation2_ToggleBtn.SetValue(False)
			self.led2_ToggleBtn.SetValue(False)

	def CheckIrrigation1Fields(self,event):
		if not self.stage1Fill1:
			print ('unable to AUTO')
			self.irrigation1_ToggleBtn.SetValue(False)

	def CheckLed1Fields(self,event):
		if not self.stage1Led1On:
			print('unable to AUTO')
			self.led1_ToggleBtn.SetValue(False)

	def CheckIrrigation2Fields(self,event):
		if not self.stage1Fill2 or self.singleChannelMode_CheckBox.GetValue() == True:
			print ('unable to AUTO')
			self.irrigation2_ToggleBtn.SetValue(False)

	def CheckLed2Fields(self,event):
		if not self.stage1Led2On or self.singleChannelMode_CheckBox.GetValue() == True:
			print('unable to AUTO')
			self.led2_ToggleBtn.SetValue(False)

	def CheckDoserFields(self,event):
		if not self.stage1Topup:
			print('unable to AUTO')
			self.doser_ToggleBtn.SetValue(False)

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
