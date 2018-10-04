import wx
import gui_irrigation_s1_7 as gui
import time
import datetime
import serial

class Irrigation(gui.GuiFrame):
	def __init__(self,parent):
		gui.GuiFrame.__init__(self,parent)
		self.timeNow, self.dateNow = '', ''
		self.ser = serial.Serial() # create serial object without port address first
		self.ser.baudrate = 9600 #set serial baudrate
		self.logFile = '' #empty address
		self.pump1Stage1Pump_Timings, self.pump1Stage1Drain_Timings = [], []
		self.pump1Stage2Pump_Timings, self.pump1Stage2Drain_Timings = [], []
		self.pump1Stage3Pump_Timings, self.pump1Stage3Drain_Timings = [], []
		self.pump2Stage1Pump_Timings, self.pump2Stage1Drain_Timings = [], []
		self.pump2Stage2Pump_Timings, self.pump2Stage2Drain_Timings = [], []
		self.pump2Stage3Pump_Timings, self.pump2Stage3Drain_Timings = [], []
		self.stage1Duration, self.stage2Duration, self.stage3Duration = 0, 0, 0
		self.currentStage = 0
		self.temp1, self.temp2 = 0, 0
		self.humidity = 0

	def Tick(self,parent):
		self.TimeDateDisplay()
		self.DaysPassedDisplay()
		self.IrrigationCheck()
		self.CheckIncomingSerial()

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
			if daysPassed <= self.stage1Duration:
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

			if parameter == 'pump1_stage1_pump':
				self.pump1Stage1Pump_Timings = value.split(',')
				self.pump1Stage1Pump_Display.SetLabel(str(self.pump1Stage1Pump_Timings))
			if parameter == 'pump1_stage1_drain':
				self.pump1Stage1Drain_Timings = value.split(',')
				self.pump1Stage1Drain_Display.SetLabel(str(self.pump1Stage1Drain_Timings))
			
			if parameter == 'pump1_stage2_pump':
				self.pump1Stage2Pump_Timings = value.split(',')
				self.pump1Stage2Pump_Display.SetLabel(str(self.pump1Stage2Pump_Timings))
			if parameter == 'pump1_stage2_drain':
				self.pump1Stage2Drain_Timings = value.split(',')
				self.pump1Stage2Drain_Display.SetLabel(str(self.pump1Stage2Drain_Timings))
			
			if parameter == 'pump1_stage3_pump':
				self.pump1Stage3Pump_Timings = value.split(',')
				self.pump1Stage3Pump_Display.SetLabel(str(self.pump1Stage3Pump_Timings))
			if parameter == 'pump1_stage3_drain':
				self.pump1Stage3Drain_Timings = value.split(',')
				self.pump1Stage3Drain_Display.SetLabel(str(self.pump1Stage3Drain_Timings))

			if parameter == 'pump2_stage1_pump':
				self.pump2Stage1Pump_Timings = value.split(',')
				self.pump2Stage1Pump_Display.SetLabel(str(self.pump2Stage1Pump_Timings))
			if parameter == 'pump2_stage1_drain':
				self.pump2Stage1Drain_Timings = value.split(',')
				self.pump2Stage1Drain_Display.SetLabel(str(self.pump2Stage1Drain_Timings))
			
			if parameter == 'pump2_stage2_pump':
				self.pump2Stage2Pump_Timings = value.split(',')
				self.pump2Stage2Pump_Display.SetLabel(str(self.pump2Stage2Pump_Timings))
			if parameter == 'pump2_stage2_drain':
				self.pump2Stage2Drain_Timings = value.split(',')
				self.pump2Stage2Drain_Display.SetLabel(str(self.pump2Stage2Drain_Timings))
			
			if parameter == 'pump2_stage3_pump':
				self.pump2Stage3Pump_Timings = value.split(',')
				self.pump2Stage3Pump_Display.SetLabel(str(self.pump2Stage3Pump_Timings))
			if parameter == 'pump2_stage3_drain':
				self.pump2Stage3Drain_Timings = value.split(',')
				self.pump2Stage3Drain_Display.SetLabel(str(self.pump2Stage3Drain_Timings))

			if parameter == 'stage1_duration':
				self.stage1Duration = int(value)
				self.stage1Duration_Display.SetLabel(str(self.stage1Duration))
			if parameter == 'stage2_duration':
				self.stage2Duration = int(value)
				self.stage2Duration_Display.SetLabel(str(self.stage2Duration))
			if parameter == 'stage3_duration':
				self.stage3Duration = int(value)
				self.stage3Duration_Display.SetLabel(str(self.stage3Duration))

	def ConnectSerial(self,event):
		serialAddress = self.serialPort_Cbox.GetValue()
		self.ser.port = str(serialAddress) #define serial port address here
		try:
			self.ser.open() #open serial port
		except:
			self.connectedPort_Display.SetLabel('failed')
		else:
			self.connectedPort_Display.SetLabel(serialAddress)

	def SendSerial(self,event):
		serialInput = self.serialInput_Txtctrl.GetValue()
		if serialInput == '':
			print('no message')
		else:
			try:
				self.ser.write(serialInput.encode())
			except:
				print('unable to send serial data')

	def LoadLog(self,event):
		with wx.FileDialog(self, "Open Text file", wildcard="Text files (*.txt)|*.txt",\
			style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			self.logFile = fileDialog.GetPath()
			logFileSplit = self.logFile.split('/') #split the path
			self.log_Display.SetLabel(logFileSplit[-1]) # only display the file name from the path

	def IrrigationCheck(self):
		if self.autoPump1_ToggleBtn.GetValue() == True:
			if self.currentStage == 1:
				for thisTime in self.pump1Stage1Pump_Timings:
					if thisTime == self.timeNow:
						self.PumpFunction(1,1)
				for thisTime in self.pump1Stage1Drain_Timings:
					if thisTime == self.timeNow:
						self.DrainFunction(1,1)
				
			elif self.currentStage == 2:
				for thisTime in self.pump1Stage2Pump_Timings:
					if thisTime == self.timeNow:
						self.self.PumpFunction(1,1)
				for thisTime in self.pump1Stage2Drain_Timings:
					if thisTime == self.timeNow:
						self.DrainFunction(1,1)

			elif self.currentStage == 3:
				for thisTime in self.pump1Stage3Pump_Timings:
					if thisTime == self.timeNow:
						self.PumpFunction(1,1)
				for thisTime in self.pump1Stage3Drain_Timings:
					if thisTime == self.timeNow:
						self.DrainFunction(1,1)

		elif self.autoPump2_ToggleBtn.GetValue() == True:
			if self.currentStage == 1:
				for thisTime in self.pump2Stage1Pump_Timings:
					if thisTime == self.timeNow:
						self.PumpFunction(2,1)
				for thisTime in self.pump2Stage1Drain_Timings:
					if thisTime == self.timeNow:
						self.DrainFunction(2,1)

			if self.currentStage == 2:
				for thisTime in self.pump2Stage2Pump_Timings:
					if thisTime == self.timeNow:
						self.PumpFunction(2,1)
				for thisTime in self.pump2Stage2Drain_Timings:
					if thisTime == self.timeNow:
						self.DrainFunction(2,1)

			if self.currentStage == 3:
				for thisTime in self.pump2Stage3Pump_Timings:
					if thisTime == self.timeNow:
						self.PumpFunction(2,1)
				for thisTime in self.pump2Stage3Drain_Timings:
					if thisTime == self.timeNow:
						self.DrainFunction(2,1)

	def PumpFunction(self,pump,state):
			self.ser.write(('PU{} {}'.format(pump,state)).encode())
			print ('PU{} {}'.format(pump,state))

	def DrainFunction(self,drain,state):
		self.ser.write(('DR{} {}'.format(pump,state)).encode())

	def CheckIrrigation1Fields(self,event):
		if self.ser.isOpen() == False or not self.pump1Stage1Pump_Timings:
			print ('unable to AUTO')
			self.autoPump1_ToggleBtn.SetValue(False)

	def CheckIrrigation2Fields(self,event):
		if self.ser.isOpen() == False or not self.pump2Stage1Pump_Timings:
			print ('unable to AUTO')
			self.autoPump2_ToggleBtn.SetValue(False)

	def CheckIncomingSerial(self):
		try:
			rawData = self.ser.readLine()
			rawData = rawData.decode('utf-8')
			rawData = rawData[:-2]
			rawDataList = rawData.split(' ')
			dataType = rawDataList[0]
			value = float(rawDataList[1])
		except:
			pass
		else:
			self.CheckData(dataType,value)

	def CheckData(self,dataType,value):
		if dataType == 'TP1' or dataType == 'TP2':
			self.ShowTemperature(dataType,value)
		elif dataType == 'HM1':
			self.ShowHumidity(value)

	def ShowTemperature(self,sensor,temperature):
		if sensor == 'TP1':
			self.temp1 = temperature
			self.temp1_Display.SetLabel(str(self.temp1))
		elif sensor == 'TP2':
			self.temp2 = temperature
			self.temp2_Display.SetLabel(str(self.temp2))
		tempA = round (((self.temp1 + self.temp2)/2),2)
		tempA_Display.SetLabel(str(tempA))

	def ShowHumidity(self,humidity):
		self.humidity = humidity
		self.humidity_Display.SetLabel(self.humidity)

	def UpdateSensorsIntervals(self,event):
		if self.tempInterval_Txtctrl.GetValue() != '' and self.humidityInterval_Txtctrl.GetValue() != '':
			tempInterval = self.tempInterval_Txtctrl.GetValue()
			humidityInterval = self.humidityInterval_Txtctrl.GetValue()
			try:
				self.ser.write(('TP0 {}\r\n'.format(tempInterval)).encode())
				self.ser.write(('HM0 {}'.format(humidityInterval)).encode())
			except:
				print('no serial connection')

app = wx.App(False)
frame = Irrigation(None)
frame.Show(True)
app.MainLoop()
