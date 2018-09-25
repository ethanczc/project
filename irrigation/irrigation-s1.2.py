from tkinter import*
import time
import threading
import serial
import datetime
import smtplib

root= Tk()
root.title('serial test')
root.geometry('1000x700')

ser = serial.Serial('/dev/ttyUSB0',9600)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ethanczc.rpi@gmail.com','zaq1@wsx')

# **************** time block start ***************

clockLabel = Label(root, text='clock',font=('times',16)).grid(row=0,column=0, padx=5,pady=5)
clock = Label(root, font=('times', 20, 'bold'), bg='white')
clock.grid(row=0,column=1,pady=5, padx=5)

currentDateLabel = Label(root,text='Current Date').grid(row=1,column=0)
currentDateDisplay = Label(root,text='1')
currentDateDisplay.grid(row=1,column=1)

startDateLabel = Label(root,text='Start Date').grid(row=2, column=0)
startDateEntry = Entry(root)
startDateEntry.grid(row=2,column=1)

daysPassedLabel = Label(root,text='Days Passed').grid(row=3,column=0)
daysPassedDisplay = Label(root,text='1',)
daysPassedDisplay.grid(row=3,column=1)

currentStageLabel = Label(root,text='Current Stage').grid(row=4,column=0)
currentStageDisplay = Label(root,text='1',font=('times', 12, 'bold'), bg='black', fg='white')
currentStageDisplay.grid(row=4,column=1)

# ********************* time block end ****************

# ********************* serial control start **********

serialControlLabel = Label(root,text='SERIAL CONTROL').grid(row=8,column=0,columnspan=2)

serialStatusLabel = Label(root, text='Serial Status').grid(row=9,column=0)
serialStatusDisplay = Label(root, text = 'Disconnected')
serialStatusDisplay.grid(row=9, column=1)

serialEntryLabel = Label(root, text='Serial Command').grid(row=10,column=0)
serialEntry = Entry(root)
serialEntry.grid(row=10, column=1)

def SendSerial():
    try:
        message = serialEntry.get()
    except:
        pass
    else:
        ser.write(message.encode()) #encode message before sending to arduino

serialSendButton = Button(root, text='send serial', command = SendSerial)
serialSendButton.grid(row=11,column=0,columnspan=2)

blankSpace1Label = Label(root,text='').grid(row=12,column=0,columnspan=6)

# ********************** serial control end ********************

# ********************** light control start *******************

lightControlLabel = Label(root,text='LIGHTS CONTROL').grid(row=0,column=2,columnspan=2)

lightOnLabel = Label(root,text='Lights ON').grid(row=1,column=2)
lightOnEntry = Entry(root)
lightOnEntry.grid(row=1,column=3)

lightOffLabel = Label(root,text='Lights OFF').grid(row=2,column=2)
lightOffEntry = Entry(root)
lightOffEntry.grid(row=2,column=3)

lightOnTimings = []
lightOffTimings = []

def UpdateLightTimings():
    global lightOnTimings, lightOffTimings
    
    lightOnInput = lightOnEntry.get()
    lightOnTimings = lightOnInput.split(' , ')
    
    lightOffInput = lightOffEntry.get()
    lightOffTimings = lightOffInput.split(' , ')
    
    print(lightOnTimings)
    print(lightOffTimings)
    
UpdateLightButton = Button(root, text='Update Light Timings',command=UpdateLightTimings)
UpdateLightButton.grid(row=3,column=2,columnspan=2)

lightAutoManualState = False

def ChangeLightAutoManualState():
    global lightAutoManualState
    lightAutoManualState = not lightAutoManualState
    if (lightAutoManualState == True):
        lightAutoManualStateDisplay.config(text='AUTO LIGHTS', fg= 'blue')
    else:
        lightAutoManualStateDisplay.config(text='MANUAL LIGHTS', fg='red')

lightAutoManualButton = Button(root, text = 'Auto/Manual Toggle', command=ChangeLightAutoManualState)
lightAutoManualButton.grid(row=4, column=2)

lightAutoManualStateDisplay = Label(root, text='MANUAL LIGHTS',fg='red')
lightAutoManualStateDisplay.grid(row=4, column=3)

lightState = False

def CheckLightActivation():
    global lightAutoManualState, lightOnTimings, lightOffTimings, lightState
    while True:
        if lightAutoManualState == True:
            timeNow = time.strftime('%H:%M:%S')
            for thisTime in lightOnTimings:
                if thisTime == timeNow:
                    LightActivation(True)
                    lightState = True
            for thisTime in lightOffTimings:
                if thisTime == timeNow:
                    LightActivation(False)
                    lightState = False
        time.sleep(1)

def LightActivation(state):

    if state == True:
        ser.write(('LT1 1').encode())
    else:
        ser.write(('LT1 0').encode())
        
def ManualLightToggle():
    global lightAutoManualState, lightState
    if lightAutoManualState == False:
        lightState = not lightState
        if lightState == True:
            LightActivation(True)
        else:
            LightActivation(False)

lightToggleLabel = Label(root,text='Manual Light On/Off Toggle').grid(row=5,column=2)
lightToggleButton = Button(root,text='TOGGLE',command=ManualLightToggle)
lightToggleButton.grid(row=5,column=3)

# ************************** light control end **********************

# ************************** fan control start **********************

fanControlLabel = Label (root,text='FAN CONTROL').grid(row=7,column=2,columnspan=2)
fanAutoOnTempLabel = Label(root,text='Upper Temp').grid(row=8,column=2)
fanAutoOnTempEntry = Entry(root)
fanAutoOnTempEntry.grid(row=8,column=3)

fanAutoOffTempLabel = Label(root,text='Lower Temp').grid(row=9,column=2)
fanAutoOffTempEntry = Entry(root)
fanAutoOffTempEntry.grid(row=9,column=3)

fanAutoEnabled = BooleanVar()

fanAutoManualCheckbox = Checkbutton(root,text='Enable Auto Fan',
                                    variable = fanAutoEnabled)
fanAutoManualCheckbox.grid(row=10,column=2,columnspan=2)

fanUpperTemp = 30.0
fanLowerTemp = 28.0

def UpdateFanAutoTemp():
    global fanUpperTemp, fanLowerTemp
    fanUpperTemp = float(fanAutoOnTempEntry.get())
    fanLowerTemp = float(fanAutoOffTempEntry.get())
    print('upper fan temp limit = {} \r\nlower fan temp limit = {}'.format(fanUpperTemp,fanLowerTemp))
                                 
updateFanAutoTempButton = Button(root,text='Update Fan Parameters', command=UpdateFanAutoTemp)
                                 
updateFanAutoTempButton.grid(row=11,column=2,columnspan=2)

fanAutoIntervalCheck = 5

def CheckFanActivation():
    global fanAutoEnabled, tempAvg, fanUpperTemp, fanLowerTemp, fanAutoIntervalCheck
    while True:
        if fanAutoEnabled.get() == True:
            if tempAvg > fanUpperTemp:
                ser.write(('FN1 1').encode())
                print('fan on')
            elif tempAvg < fanLowerTemp:
                ser.write(('FN1 0').encode())
                print('fan off')
        time.sleep(fanAutoIntervalCheck)

# ************************* fan control end ********************

# ************************* sensor control start ********************

sensorsLabel = Label(root,text='SENSORS').grid(row=0,column=4,columnspan=2)

temp1Label = Label(root, text = 'Temp1').grid(row=1,column=4)
temp1Display = Label(root, text= '')
temp1Display.grid(row=1, column=5)

temp2Label = Label(root, text = 'Temp2').grid(row=2,column=4)
temp2Display = Label(root, text= '')
temp2Display.grid(row=2, column=5)

tempAvgLabel = Label(root, text = 'A.Temp').grid(row=3,column=4)
tempAvgDisplay = Label(root, text= '')
tempAvgDisplay.grid(row=3, column=5)

tempIntervalLabel = Label(root, text='Temp interval (seconds)').grid(row=4,column=4)
tempIntervalEntry = Entry(root)
tempIntervalEntry.grid(row=4,column=5)

humidityLabel = Label(root, text = 'Humidity').grid(row=5,column=4)
humidityDisplay = Label(root,text='')
humidityDisplay.grid(row=5,column=5)

humdityIntervalLabel = Label(root, text='Humidity interval (mins)').grid(row=6,column=4)
humidityIntervalEntry = Entry(root)
humidityIntervalEntry.grid(row=6,column=5)

distanceDisplayLabel = Label(root, text = 'Waterlevel').grid(row=7,column=4)
distanceDisplay = Label(root,text='')
distanceDisplay.grid(row=7,column=5)

distanceLabel = Label(root, text='Waterlevel (time)').grid(row=8,column=4)
distanceTimingEntry = Entry(root)
distanceTimingEntry.grid(row=8,column=5)

distanceAlarmLabel = Label(root,text='Max Distance').grid(row=9,column=4)
distanceAlarmEntry = Entry(root)
distanceAlarmEntry.grid(row=9,column=5)

alarmNotificationsEnabled = BooleanVar()

enabledAlarmNotifications_Checkbox = Checkbutton(root,text='Enable Email Notifications',
                                                 variable=alarmNotificationsEnabled)
enabledAlarmNotifications_Checkbox.grid(row=10,column=4,columnspan=2)

distanceTiming = []
distanceAlarm = 10.0

def UpdateSensorsParameters():
    global distanceTiming, distanceAlarm
    try:
        tempInterval = tempIntervalEntry.get()
        humidityInterval = humidityIntervalEntry.get()
        distanceInterval = distanceTimingEntry.get()
    except:
        pass
    else:
        ser.write(('TP0 {}\r\n'.format(tempInterval)).encode())
        ser.write(('HM0 {}'.format(humidityInterval)).encode())
        distanceTiming = (distanceTimingEntry.get()).split(' , ')
        distanceAlarm = float(distanceAlarmEntry.get())
        print(distanceTiming)
        
updateSensorsParametersButton = Button(root, text = 'Update Sensors Parameters',command=UpdateSensorsParameters)
updateSensorsParametersButton.grid(row=11,column=4,columnspan=2)
        
def GetDistanceSensors():
    global distanceTiming, distanceAlarm
    while True:
        timeNow = time.strftime('%H:%M:%S')
        for thisTime in distanceTiming:
            if thisTime == timeNow:
                ser.write(('DT1 1').encode())
        time.sleep(1)
        
def CheckDistanceAlarm(measuredDistance):
    
    global distanceAlarm, alarmNotificationsEnabled
    if measuredDistance > distanceAlarm:
        distanceDisplay.config(text = measuredDistance, fg='red')
    else:
            distanceDisplay.config(text = measuredDistance, fg='green')
    if alarmNotificationsEnabled.get() == True:
        if measuredDistance > distanceAlarm:
            warningMsg = 'The water level is low, measured at {}'.format(measuredDistance)
            server.sendmail('ethanczc.rpi@gmail.com','ethanczc.rpi@gmail.com',warningMsg)
            
# *********************** sensor block end *********************

# *********************** pump 1 control start *******************

pump1ControlLabel = Label(root,text='PUMP 1 CONTROL').grid(row=14,column=0,columnspan=2)

pump1Stage1_Label = Label(root,text='STAGE 1').grid(row=15,column=0,columnspan=2)

pump1Stage1_OnLabel = Label(root,text='Stage 1 ON').grid(row=16,column=0)
pump1Stage1_OnEntry = Entry(root)
pump1Stage1_OnEntry.grid(row=16,column=1)

pump1Stage1_OffLabel = Label(root,text='Stage 1 DRAIN').grid(row=17,column=0)
pump1Stage1_OffEntry = Entry(root)
pump1Stage1_OffEntry.grid(row=17,column=1)

pump1Stage1_DurationLabel = Label(root,text='Stage 1 Duration').grid(row=18,column=0)
pump1Stage1_DurationEntry = Entry(root)
pump1Stage1_DurationEntry.grid(row=18,column=1)

pump1Stage2_Label = Label(root,text='STAGE 2').grid(row=19,column=0,columnspan=2)

pump1Stage2_OnLabel = Label(root,text='Stage 2 ON').grid(row=20,column=0)
pump1Stage2_OnEntry = Entry(root)
pump1Stage2_OnEntry.grid(row=20,column=1)

pump1Stage2_OffLabel = Label(root,text='Stage 2 DRAIN').grid(row=21,column=0)
pump1Stage2_OffEntry = Entry(root)
pump1Stage2_OffEntry.grid(row=21,column=1)

pump1Stage2_DurationLabel = Label(root,text='Stage 2 Duration').grid(row=22,column=0)
pump1Stage2_DurationEntry = Entry(root)
pump1Stage2_DurationEntry.grid(row=22,column=1)

pump1Stage2_Label = Label(root,text='STAGE 3').grid(row=23,column=0,columnspan=2)

pump1Stage3_OnLabel = Label(root,text='Stage 3 ON').grid(row=24,column=0)
pump1Stage3_OnEntry = Entry(root)
pump1Stage3_OnEntry.grid(row=24,column=1)

pump1Stage3_OffLabel = Label(root,text='Stage 3 DRAIN').grid(row=25,column=0)
pump1Stage3_OffEntry = Entry(root)
pump1Stage3_OffEntry.grid(row=25,column=1)

pump1Stage3_DurationLabel = Label(root,text='Stage 3 Duration').grid(row=26,column=0)
pump1Stage3_DurationEntry = Entry(root)
pump1Stage3_DurationEntry.grid(row=26,column=1)

pump1Drain_DurationLabel = Label(root,text='Drain Duration').grid(row=27,column=0)
pump1Drain_DurationEntry = Entry(root)
pump1Drain_DurationEntry.grid(row=27,column=1)

pump1Stage1_OnTimings = []
pump1Stage1_OffTimings = []
pump1Stage2_OnTimings = []
pump1Stage2_OffTimings = []
pump1Stage3_OnTimings = []
pump1Stage3_OffTimings = []
pump1Stage1_Duration = 0
pump1Stage2_Duration = 0
pump1Stage3_Duration = 0
pump1Drain_Duration = 0

def UpdatePump1Timings():
    global pump1Stage1_OnTimings, pump1Stage1_OffTimings, pump1Stage2_OnTimings, pump1Stage2_OffTimings, pump1Stage3_OnTimings, pump1Stage3_OffTimings
    global pump1Stage1_Duration,pump1Stage2_Duration,pump1Stage3_Duration, pump1Drain_Duration
    
    pump1Stage1_OnInput = pump1Stage1_OnEntry.get()
    pump1Stage1_OnTimings = pump1Stage1_OnInput.split(' , ')
    pump1Stage1_OffInput = pump1Stage1_OffEntry.get()
    pump1Stage1_OffTimings = pump1Stage1_OffInput.split(' , ')
    
    pump1Stage2_OnInput = pump1Stage2_OnEntry.get()
    pump1Stage2_OnTimings = pump1Stage2_OnInput.split(' , ')
    pump1Stage2_OffInput = pump1Stage2_OffEntry.get()
    pump1Stage2_OffTimings = pump1Stage2_OffInput.split(' , ')
    
    pump1Stage3_OnInput = pump1Stage3_OnEntry.get()
    pump1Stage3_OnTimings = pump1Stage3_OnInput.split(' , ')
    pump1Stage3_OffInput = pump1Stage3_OffEntry.get()
    pump1Stage3_OffTimings = pump1Stage3_OffInput.split(' , ')
    
    pump1Stage1_Duration = int(pump1Stage1_DurationEntry.get())
    pump1Stage2_Duration = int(pump1Stage2_DurationEntry.get())
    pump1Stage3_Duration = int(pump1Stage3_DurationEntry.get())
    
    pump1Drain_Duration = int(pump1Drain_DurationEntry.get())
    ser.write(('DR0 {}'.format(pump1Drain_Duration)).encode())
    
    print(pump1Stage1_OnTimings)
    print(pump1Stage1_OffTimings)
    print(pump1Stage2_OnTimings)
    print(pump1Stage2_OffTimings)
    print(pump1Stage3_OnTimings)
    print(pump1Stage3_OffTimings)
    print(pump1Drain_Duration)

UpdatePump1Button = Button(root, text='Update Pump Parameters',command=UpdatePump1Timings)
UpdatePump1Button.grid(row=28,column=0,columnspan=2)

currentStage = 1

def DisplayCurrentStage():
    global pump1Stage1_Duration,pump1Stage2_Duration,pump1Stage3_Duration,currentStage, daysPassed
    if daysPassed <= pump1Stage1_Duration:
        currentStage =1
    elif pump1Stage1_Duration <= daysPassed <= (pump1Stage1_Duration + pump1Stage2_Duration):
        currentStage =2
    elif (pump1Stage1_Duration + pump1Stage2_Duration) <= daysPassed <= (pump1Stage1_Duration + pump1Stage2_Duration + pump1Stage3_Duration):
        currentStage =3
    currentStageDisplay.config(text=currentStage)
    
pumpAutoManualState = False

def CheckPumpsActivation():
    global pumpAutoManualState, pump1Stage1_OnTimings, pump1Stage1_OffTimings, pump1Stage2_OnTimings, pump1Stage2_OffTimings, pump1Stage3_OnTimings, pump1Stage3_OffTimings
    while True:
        if pumpAutoManualState == True:
            timeNow = time.strftime('%H:%M:%S')
            if currentStage == 1:
                for thisTime in pump1Stage1_OnTimings:
                    if thisTime == timeNow:
                        PumpActivation(1,1)
                for thisTime in pump1Stage1_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(1,1)
            elif currentStage == 2:
                for thisTime in pump1Stage2_OnTimings:
                    if thisTime == timeNow:
                        PumpActivation(1,1)
                for thisTime in pump1Stage2_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(1,1)
            elif currentStage == 3:
                for thisTime in pump1Stage3_OnTimings:
                    if thisTime == timeNow:
                        PumpActivation(1,1)
                for thisTime in pump1Stage3_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(1,1)
        time.sleep(1)
        
def PumpActivation(pump, state):
    ser.write(('PU{} {}'.format(pump,state)).encode())

def DrainActivation(pump, state):
    ser.write(('DR{} {}'.format(pump,state)).encode())
            
def ChangePumpAutoManualState():
    global pumpAutoManualState
    pumpAutoManualState = not pumpAutoManualState
    if (pumpAutoManualState == True):
        pumpAutoManualStateDisplay.config(text='AUTO PUMP 1', fg= 'blue')
    else:
        pumpAutoManualStateDisplay.config(text='MANUAL PUMP 1', fg='red')

pumpAutoManualButton = Button(root, text = 'Auto/Manual Toggle', command=ChangePumpAutoManualState)
pumpAutoManualButton.grid(row=29, column=0)

pumpAutoManualStateDisplay = Label(root, text='MANUAL PUMP 1',fg='red')
pumpAutoManualStateDisplay.grid(row=29, column=1)

#  ******************************** pump control end *********************
    
def DisplayTime():
    while True:
        timeNow = time.strftime('%H:%M:%S')
        dateNow = time.strftime('%d/%m/%y')
        clock.config(text=timeNow)
        currentDateDisplay.config(text=dateNow)
        DisplayDaysPassed()
        DisplayCurrentStage()
        time.sleep(1)
   
daysPassed = 0

def DisplayDaysPassed():
    global daysPassed
    today = datetime.date.today()
    try:
        dateStartInput = (startDateEntry.get()).split('/')
        day = int(dateStartInput[0])
        month = int(dateStartInput[1])
        year = int(dateStartInput[2])
        dateStart = datetime.date(year,month,day)
        daysPassed = (today-dateStart).days
        daysPassedDisplay.config(text=daysPassed)
        #print('days difference = {}'.format(daysPassed))
    except:
        pass
    
def CheckIncomingSerial():
    while True:
        try:
            rawData = ser.readline()
            rawData = rawData.decode('utf-8') #decode message from arduino
            rawData = rawData[:-2] #splice off \r\n
            print('raw data received is {}'.format(rawData))
            rawDataList = rawData.split(' ')
            command = rawDataList[0]
            value = float(rawDataList[1])
        except:
            pass
        else:
            processedData = [command,value]
            print('processed data from raw data is {}'.format(processedData))
            CheckData(processedData)
            
def CheckSerialStatus():
    while True:
        try:
            serialStatus = ser.isOpen()
        except:
            pass
        else:
            if serialStatus == True:
                serialStatusDisplay.config(text='connected')
            else:
                serialStatusDisplay.config(text='disconnected')
        finally:
            time.sleep(1)
    
def CheckData(processedData):
        
    if processedData[0] == 'TP1' or processedData[0] == 'TP2': 
        ShowTemperature(processedData[0],processedData[1])
    elif processedData[0] == 'HM1':
        humidityDisplay.config(text = processedData[1])   
    elif processedData[0] == 'DT1':
        CheckDistanceAlarm(processedData[1])
        
temp1 = 0
temp2 = 0
tempAvg = 0

def ShowTemperature(sensor,temperature):
    global temp1, temp2, tempAvg
    if sensor == 'TP1':
        temp1Display.config(text=temperature)
        temp1 = temperature
    elif sensor == 'TP2':
        temp2Display.config(text=temperature)
        temp2 = temperature
    tempAvg = round ((( temp1 + temp2 ) / 2),2)
    tempAvgDisplay.config(text=tempAvg)

def main():
    checkIncomingSerialThread = threading.Thread(name='serialCheck',target=CheckIncomingSerial, daemon=True)
    checkIncomingSerialThread.start()
    checkSerialStatusThread = threading.Thread(name='serialCheck',target=CheckSerialStatus, daemon=True)
    checkSerialStatusThread.start()
    lightActivationThread = threading.Thread(name='lightActivationCheck',target=CheckLightActivation, daemon=True)
    lightActivationThread.start()
    pumpsActivationThread = threading.Thread(name='pumpActivationCheck',target=CheckPumpsActivation, daemon=True)
    pumpsActivationThread.start()
    getSensorsThread = threading.Thread(name='sensorActivationCheck',target=GetDistanceSensors, daemon=True)
    getSensorsThread.start()
    fanActivationThread = threading.Thread(name='fanActivationCheck',target=CheckFanActivation, daemon=True)
    fanActivationThread.start()
    showTime = threading.Thread(name='serialCheck',target=DisplayTime, daemon=True)
    showTime.start()
    root.mainloop()

if __name__ == '__main__':
    main()
