from tkinter import*
import time
import threading
import serial
import datetime
import smtplib
#look into prevent 2 threads from serial writing to the serial port at the same time
#this code is for USB1, and logging to event_log1.txt
root= Tk()
root.title('serial test 5')
root.geometry('1000x700')

ser = serial.Serial('/dev/ttyUSB1',9600)

targetEmail = 'ethanczc@gmail.com'

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
lightOnEntry.insert(END,'07:01:00')
lightOnEntry.grid(row=1,column=3)

lightOffLabel = Label(root,text='Lights OFF').grid(row=2,column=2)
lightOffEntry = Entry(root)
lightOffEntry.insert(END,'19:01:00')
lightOffEntry.grid(row=2,column=3)

lightOnTimings = []
lightOffTimings = []

def UpdateLightTimings():
    global lightOnTimings, lightOffTimings
    try:
        lightOnTimings = (lightOnEntry.get()).split(' , ')
        lightOffTimings = (lightOffEntry.get()).split(' , ')
    except:
        pass
    else:
        print(str(lightOnTimings) + '\r\n' + str(lightOffTimings))
    
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
    try:
        fanUpperTemp = float(fanAutoOnTempEntry.get())
        fanLowerTemp = float(fanAutoOffTempEntry.get())
    except:
        pass
    else:
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
tempIntervalEntry.insert(END,'60')
tempIntervalEntry.grid(row=4,column=5)

humidityLabel = Label(root, text = 'Humidity').grid(row=5,column=4)
humidityDisplay = Label(root,text='')
humidityDisplay.grid(row=5,column=5)

humdityIntervalLabel = Label(root, text='Humidity interval (mins)').grid(row=6,column=4)
humidityIntervalEntry = Entry(root)
humidityIntervalEntry.insert(END,'1')
humidityIntervalEntry.grid(row=6,column=5)

distanceDisplayLabel = Label(root, text = 'Waterlevel').grid(row=7,column=4)
distanceDisplay = Label(root,text='')
distanceDisplay.grid(row=7,column=5)

distanceLabel = Label(root, text='Waterlevel (time)').grid(row=8,column=4)
distanceTimingEntry = Entry(root)
distanceTimingEntry.insert(END,'06:01:00 , 20:01:00')
distanceTimingEntry.grid(row=8,column=5)

distanceLimitLabel = Label(root,text='Max Distance').grid(row=9,column=4)
distanceLimitEntry = Entry(root)
distanceLimitEntry.insert(END,'20')
distanceLimitEntry.grid(row=9,column=5)

alarmNotificationsEnabled = BooleanVar()

enabledAlarmNotifications_Checkbox = Checkbutton(root,text='Enable Email Notifications',
                                                 variable=alarmNotificationsEnabled)
enabledAlarmNotifications_Checkbox.grid(row=10,column=4,columnspan=2)

distanceTiming = []
distanceLimit = 10.0

def UpdateSensorsParameters():
    global distanceTiming, distanceLimit
    try:
        tempInterval = tempIntervalEntry.get()
        humidityInterval = humidityIntervalEntry.get()
        distanceTiming = (distanceTimingEntry.get()).split(' , ')
    except:
        pass
    else:
        ser.write(('TP0 {}\r\n'.format(tempInterval)).encode())
        ser.write(('HM0 {}'.format(humidityInterval)).encode()) 
        distanceLimit = float(distanceLimitEntry.get())
        print(distanceTiming)
        
updateSensorsParametersButton = Button(root, text = 'Update Sensors Parameters',command=UpdateSensorsParameters)
updateSensorsParametersButton.grid(row=11,column=4,columnspan=2)
        
def GetDistanceSensors():
    global distanceTiming, distanceLimit
    while True:
        timeNow = time.strftime('%H:%M:%S')
        for thisTime in distanceTiming:
            if thisTime == timeNow:
                ser.write(('DT1 1').encode())
        time.sleep(1)

def CheckDistanceLimit(measuredDistance):
    
    global distanceLimit, alarmNotificationsEnabled
    if measuredDistance > distanceLimit:
        distanceDisplay.config(text = measuredDistance, fg='red')
    else:
            distanceDisplay.config(text = measuredDistance, fg='green')
    if alarmNotificationsEnabled.get() == True:
        if measuredDistance > distanceLimit:
            warningMsg = 'The water level is low, measured at {}'.format(measuredDistance)
            server.sendmail('ethanczc.rpi@gmail.com',targetEmail,warningMsg)
          
# *********************** sensor control end *********************

# *********************** pump 1 control start *******************

pump1ControlLabel = Label(root,text='PUMP 1 CONTROL').grid(row=14,column=0,columnspan=2)

pump1Stage1_Label = Label(root,text='STAGE 1').grid(row=15,column=0,columnspan=2)

pump1Stage1_OnLabel = Label(root,text='Stage 1 ON').grid(row=16,column=0)
pump1Stage1_OnEntry = Entry(root)
pump1Stage1_OnEntry.insert(END,'08:00:00 , 16:00:00')
pump1Stage1_OnEntry.grid(row=16,column=1)

pump1Stage1_OffLabel = Label(root,text='Stage 1 DRAIN').grid(row=17,column=0)
pump1Stage1_OffEntry = Entry(root)
pump1Stage1_OffEntry.insert(END,'08:15:00 , 16:15:00')
pump1Stage1_OffEntry.grid(row=17,column=1)

pump1Stage1_DurationLabel = Label(root,text='Stage 1 Duration').grid(row=18,column=0)
pump1Stage1_DurationEntry = Entry(root)
pump1Stage1_DurationEntry.insert(END,'4')
pump1Stage1_DurationEntry.grid(row=18,column=1)

pump1Stage2_Label = Label(root,text='STAGE 2').grid(row=19,column=0,columnspan=2)

pump1Stage2_OnLabel = Label(root,text='Stage 2 ON').grid(row=20,column=0)
pump1Stage2_OnEntry = Entry(root)
pump1Stage2_OnEntry.insert(END,'08:00:00 , 11:00:00 , 14:00:00 , 17:00:00')
pump1Stage2_OnEntry.grid(row=20,column=1)

pump1Stage2_OffLabel = Label(root,text='Stage 2 DRAIN').grid(row=21,column=0)
pump1Stage2_OffEntry = Entry(root)
pump1Stage2_OffEntry.insert(END,'08:15:00 , 11:15:00 , 14:15:00 , 17:15:00')
pump1Stage2_OffEntry.grid(row=21,column=1)

pump1Stage2_DurationLabel = Label(root,text='Stage 2 Duration').grid(row=22,column=0)
pump1Stage2_DurationEntry = Entry(root)
pump1Stage2_DurationEntry.insert(END,'4')
pump1Stage2_DurationEntry.grid(row=22,column=1)

pump1Stage2_Label = Label(root,text='STAGE 3').grid(row=23,column=0,columnspan=2)

pump1Stage3_OnLabel = Label(root,text='Stage 3 ON').grid(row=24,column=0)
pump1Stage3_OnEntry = Entry(root)
pump1Stage3_OnEntry.insert(END,'00:00:00 , 00:40:00 , 01:00:00 , 01:40:00 , 02:00:00 , 02:40:00 , 03:00:00 , 03:40:00 , \
	04:00:00 , 04:40:00 , 05:00:00 , 05:40:00 , 06:00:00 , 06:40:00 , 07:00:00 , 07:40:00 , 08:00:00 , 08:40:00 , \
	09:00:00 , 09:40:00 , 10:00:00 , 10:40:00 , 11:00:00 , 11:40:00 , 12:00:00 , 12:40:00 , 13:00:00 , 13:40:00 , \
	14:00:00 , 14:40:00 , 15:00:00 , 15:40:00 , 16:00:00 , 16:40:00 , 17:00:00 , 17:40:00 , 18:00:00 , 18:40:00 , \
	19:00:00 , 19:40:00 , 20:00:00 , 20:40:00 , 21:00:00 , 21:40:00 , 22:00:00 , 22:40:00 , 23:00:00 , 23:40:00')
pump1Stage3_OnEntry.grid(row=24,column=1)

pump1Stage3_OffLabel = Label(root,text='Stage 3 DRAIN').grid(row=25,column=0)
pump1Stage3_OffEntry = Entry(root)
pump1Stage3_OffEntry.insert(END,'00:10:00 , 00:50:00 , 01:10:00 , 01:50:00 , 02:10:00 , 02:50:00 , 03:10:00 , 03:50:00 , \
	04:10:00 , 04:50:00 , 05:10:00 , 05:50:00 , 06:10:00 , 06:50:00 , 07:10:00 , 07:50:00 , 08:10:00 , 08:50:00 , \
	09:10:00 , 09:50:00 , 10:10:00 , 10:50:00 , 11:10:00 , 11:50:00 , 12:10:00 , 12:50:00 , 13:10:00 , 13:50:00 , \
	14:10:00 , 14:50:00 , 15:10:00 , 15:50:00 , 16:10:00 , 16:50:00 , 17:10:00 , 17:50:00 , 18:10:00 , 18:50:00 , \
	19:10:00 , 19:50:00 , 20:10:00 , 20:50:00 , 21:10:00 , 21:50:00 , 22:10:00 , 22:50:00 , 23:10:00 , 23:50:00')
pump1Stage3_OffEntry.grid(row=25,column=1)

pump1Stage3_DurationLabel = Label(root,text='Stage 3 Duration').grid(row=26,column=0)
pump1Stage3_DurationEntry = Entry(root)
pump1Stage3_DurationEntry.insert(END, '40')
pump1Stage3_DurationEntry.grid(row=26,column=1)

pump1Drain_DurationLabel = Label(root,text='Drain Duration').grid(row=27,column=0)
pump1Drain_DurationEntry = Entry(root)
pump1Drain_DurationEntry.insert(END, '300')
pump1Drain_DurationEntry.grid(row=27,column=1)

pump1Stage1_OnTimings, pump1Stage1_OffTimings = [] , []
pump1Stage2_OnTimings, pump1Stage2_OffTimings = [] , []
pump1Stage3_OnTimings, pump1Stage3_OffTimings = [] , []
pump1Stage1_Duration, pump1Stage2_Duration = 0 , 0
pump1Stage3_Duration, pump1Drain_Duration = 0 , 0

def UpdatePump1Timings():
    global pump1Stage1_OnTimings, pump1Stage1_OffTimings, pump1Stage2_OnTimings, pump1Stage2_OffTimings, pump1Stage3_OnTimings, pump1Stage3_OffTimings
    global pump1Stage1_Duration,pump1Stage2_Duration,pump1Stage3_Duration, pump1Drain_Duration
    
    try:
        pump1Stage1_OnTimings = (pump1Stage1_OnEntry.get()).split(' , ')
        pump1Stage1_OffTimings= (pump1Stage1_OffEntry.get()).split(' , ')
        
        pump1Stage2_OnTimings = (pump1Stage2_OnEntry.get()).split(' , ')
        pump1Stage2_OffTimings= (pump1Stage2_OffEntry.get()).split(' , ')
        
        pump1Stage3_OnTimings = (pump1Stage3_OnEntry.get()).split(' , ')
        pump1Stage3_OffTimings= (pump1Stage3_OffEntry.get()).split(' , ')
        
        pump1Stage1_Duration = int(pump1Stage1_DurationEntry.get())
        pump1Stage2_Duration = int(pump1Stage2_DurationEntry.get())
        pump1Stage3_Duration = int(pump1Stage3_DurationEntry.get())
        
        pump1Drain_Duration = int(pump1Drain_DurationEntry.get())
        ser.write(('DR0 {}'.format(pump1Drain_Duration)).encode())
    except:
        pass
    else:
        print(pump1Stage1_OnTimings)
        print(pump1Stage1_OffTimings)
        print(pump1Stage2_OnTimings)
        print(pump1Stage2_OffTimings)
        print(pump1Stage3_OnTimings)
        print(pump1Stage3_OffTimings)
        print(pump1Drain_Duration)

UpdatePump1Button = Button(root, text='Update Pump 1 Parameters',command=UpdatePump1Timings)
UpdatePump1Button.grid(row=28,column=0,columnspan=2)

def ChangePump1AutoManualState():
    global pump1AutoManualState
    pump1AutoManualState = not pump1AutoManualState
    if (pump1AutoManualState == True):
        pump1AutoManualStateDisplay.config(text='AUTO PUMP 1', fg= 'blue')
    else:
        pump1AutoManualStateDisplay.config(text='MANUAL PUMP 1', fg='red')

pump1AutoManualButton = Button(root, text = 'Auto/Manual Toggle', command=ChangePump1AutoManualState)
pump1AutoManualButton.grid(row=29, column=0)

pump1AutoManualStateDisplay = Label(root, text='MANUAL PUMP 1',fg='red')
pump1AutoManualStateDisplay.grid(row=29, column=1)

pump1AutoManualState = False

#  ******************************** pump 1 control end *********************

#  ******************************** pump 2 control start *********************

pump2ControlLabel = Label(root,text='PUMP 2 CONTROL').grid(row=14,column=2,columnspan=2)

pump2Stage1_Label = Label(root,text='STAGE 1').grid(row=15,column=2,columnspan=2)

pump2Stage1_OnLabel = Label(root,text='Stage 1 ON').grid(row=16,column=2)
pump2Stage1_OnEntry = Entry(root)
pump2Stage1_OnEntry.insert(END, '08:30:00 , 16:30:00')
pump2Stage1_OnEntry.grid(row=16,column=3)

pump2Stage1_OffLabel = Label(root,text='Stage 1 DRAIN').grid(row=17,column=2)
pump2Stage1_OffEntry = Entry(root)
pump2Stage1_OffEntry.insert(END, '08:45:00 , 16:45:00')
pump2Stage1_OffEntry.grid(row=17,column=3)
'''
pump2Stage1_DurationLabel = Label(root,text='Stage 1 Duration').grid(row=18,column=2)
pump2Stage1_DurationEntry = Entry(root)
pump2Stage1_DurationEntry.grid(row=18,column=3)
'''
pump2Stage2_Label = Label(root,text='STAGE 2').grid(row=19,column=2,columnspan=2)

pump2Stage2_OnLabel = Label(root,text='Stage 2 ON').grid(row=20,column=2)
pump2Stage2_OnEntry = Entry(root)
pump2Stage2_OnEntry.insert(END, '08:30:00 , 11:30:00 , 14:30:00 , 17:30:00')
pump2Stage2_OnEntry.grid(row=20,column=3)

pump2Stage2_OffLabel = Label(root,text='Stage 2 DRAIN').grid(row=21,column=2)
pump2Stage2_OffEntry = Entry(root)
pump2Stage2_OffEntry.insert(END, '08:45:00 , 11:45:00 , 14:45:00 , 17:45:00')
pump2Stage2_OffEntry.grid(row=21,column=3)
'''
pump2Stage2_DurationLabel = Label(root,text='Stage 2 Duration').grid(row=22,column=2)
pump2Stage2_DurationEntry = Entry(root)
pump2Stage2_DurationEntry.grid(row=22,column=3)
'''
pump2Stage2_Label = Label(root,text='STAGE 3').grid(row=23,column=2,columnspan=2)

pump2Stage3_OnLabel = Label(root,text='Stage 3 ON').grid(row=24,column=2)
pump2Stage3_OnEntry = Entry(root)
pump2Stage3_OnEntry.insert(END,'00:20:00 , 01:20:00 , 02:20:00 , 03:20:00 , 04:20:00 , 05:20:00 , 06:20:00 , \
	07:20:00 , 08:20:00 , 09:20:00 , 10:20:00 , 11:20:00 , 12:20:00 , 13:20:00 , 14:20:00 , 15:20:00 , 16:20:00 , \
	17:20:00 , 18:20:00 , 19:20:00 , 20:20:00 , 21:20:00 , 22:20:00 , 23:20:00')
pump2Stage3_OnEntry.grid(row=24,column=3)

pump2Stage3_OffLabel = Label(root,text='Stage 3 DRAIN').grid(row=25,column=2)
pump2Stage3_OffEntry = Entry(root)
pump2Stage3_OffEntry.insert(END,'00:30:00 , 01:30:00 , 02:30:00 , 03:30:00 , 04:30:00 , 05:30:00 , 06:30:00 , \
	07:30:00 , 08:30:00 , 09:30:00 , 10:30:00 , 11:30:00 , 12:30:00 , 13:30:00 , 14:30:00 , 15:30:00 , 16:30:00 , \
	17:30:00 , 18:30:00 , 19:30:00 , 20:30:00 , 21:30:00 , 22:30:00 , 23:30:00')
pump2Stage3_OffEntry.grid(row=25,column=3)
'''
pump2Stage3_DurationLabel = Label(root,text='Stage 3 Duration').grid(row=26,column=2)
pump2Stage3_DurationEntry = Entry(root)
pump2Stage3_DurationEntry.grid(row=26,column=3)

pump2Drain_DurationLabel = Label(root,text='Drain Duration').grid(row=27,column=2)
pump2Drain_DurationEntry = Entry(root)
pump2Drain_DurationEntry.grid(row=27,column=3)
'''
pump2Stage1_OnTimings, pump2Stage1_OffTimings = [] , []
pump2Stage2_OnTimings, pump2Stage2_OffTimings = [] , []
pump2Stage3_OnTimings, pump2Stage3_OffTimings = [] , []
#pump2Stage1_Duration, pump2Stage2_Duration = 0 , 0
#pump2Stage3_Duration, pump2Drain_Duration = 0 , 0

def UpdatePump2Timings():
    global pump2Stage1_OnTimings, pump2Stage1_OffTimings, pump2Stage2_OnTimings, pump2Stage2_OffTimings, pump2Stage3_OnTimings, pump2Stage3_OffTimings
    #global pump2Stage1_Duration,pump2Stage2_Duration,pump2Stage3_Duration, pump2Drain_Duration
    try:
        pump2Stage1_OnTimings = (pump2Stage1_OnEntry.get()).split(' , ')
        pump2Stage1_OffTimings= (pump2Stage1_OffEntry.get()).split(' , ')
        
        pump2Stage2_OnTimings = (pump2Stage2_OnEntry.get()).split(' , ')
        pump2Stage2_OffTimings= (pump2Stage2_OffEntry.get()).split(' , ')
        
        pump2Stage3_OnTimings = (pump2Stage3_OnEntry.get()).split(' , ')
        pump2Stage3_OffTimings= (pump2Stage3_OffEntry.get()).split(' , ')
        '''
        pump2Stage1_Duration = int(pump2Stage1_DurationEntry.get())
        pump2Stage2_Duration = int(pump2Stage2_DurationEntry.get())
        pump2Stage3_Duration = int(pump2Stage3_DurationEntry.get())
        
        pump2Drain_Duration = int(pump2Drain_DurationEntry.get())
        ser.write(('DR0 {}'.format(pump2Drain_Duration)).encode())
    '''
    except:
        pass
    else:
        print(pump2Stage1_OnTimings)
        print(pump2Stage1_OffTimings)
        print(pump2Stage2_OnTimings)
        print(pump2Stage2_OffTimings)
        print(pump2Stage3_OnTimings)
        print(pump2Stage3_OffTimings)
        #print(pump2Drain_Duration)
    
UpdatePump2Button = Button(root, text='Update Pump 2 Parameters',command=UpdatePump2Timings)
UpdatePump2Button.grid(row=28,column=2,columnspan=2)

def ChangePump2AutoManualState():
    global pump2AutoManualState
    pump2AutoManualState = not pump2AutoManualState
    if (pump2AutoManualState == True):
        pump2AutoManualStateDisplay.config(text='AUTO PUMP 2', fg= 'blue')
    else:
        pump2AutoManualStateDisplay.config(text='MANUAL PUMP 2', fg='red')

pump2AutoManualButton = Button(root, text = 'Auto/Manual Toggle', command=ChangePump2AutoManualState)
pump2AutoManualButton.grid(row=29, column=2)

pump2AutoManualStateDisplay = Label(root, text='MANUAL PUMP 2',fg='red')
pump2AutoManualStateDisplay.grid(row=29, column=3)

pump2AutoManualState = False

#  ******************************** pump 2 control end *********************

#  ******************************** pump and light general control start *********************

def CheckAllActivation():
    global pump1AutoManualState, pump1Stage1_OnTimings, pump1Stage1_OffTimings, pump1Stage2_OnTimings, pump1Stage2_OffTimings, pump1Stage3_OnTimings, pump1Stage3_OffTimings
    global pump2AutoManualState, pump2Stage1_OnTimings, pump2Stage1_OffTimings, pump2Stage2_OnTimings, pump2Stage2_OffTimings, pump2Stage3_OnTimings, pump2Stage3_OffTimings
    global lightAutoManualState, lightOnTimings, lightOffTimings, lightState
    while True:
        if pump1AutoManualState == True or pump2AutoManualState == True:
            timeNow = time.strftime('%H:%M:%S')
            if currentStage == 1:
                for thisTime in pump1Stage1_OnTimings :
                    if thisTime == timeNow:
                        PumpActivation(1,1)
                for thisTime in pump1Stage1_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(1,1)
                for thisTime in pump2Stage1_OnTimings :
                    if thisTime == timeNow:
                        PumpActivation(2,1)
                for thisTime in pump2Stage1_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(2,1)
            elif currentStage == 2:
                for thisTime in pump1Stage2_OnTimings:
                    if thisTime == timeNow:
                        PumpActivation(1,1)
                for thisTime in pump1Stage2_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(1,1)
                for thisTime in pump2Stage2_OnTimings:
                    if thisTime == timeNow:
                        PumpActivation(2,1)
                for thisTime in pump2Stage2_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(2,1)
            elif currentStage == 3:
                for thisTime in pump1Stage3_OnTimings:
                    if thisTime == timeNow:
                        PumpActivation(1,1)
                for thisTime in pump1Stage3_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(1,1)
                for thisTime in pump2Stage3_OnTimings:
                    if thisTime == timeNow:
                        PumpActivation(2,1)
                for thisTime in pump2Stage3_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(2,1)

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

def PumpActivation(pump, state):
    ser.write(('PU{} {}'.format(pump,state)).encode())

def DrainActivation(pump, state):
    ser.write(('DR{} {}'.format(pump,state)).encode())
    
#  ******************************** pump general control end *********************
    
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
            rawDataList = rawData.split(' ')
            command = rawDataList[0]
            value = float(rawDataList[1])
        except:
            pass
        else:
            processedData = [command,value]
            print(processedData)
            CheckData(processedData)

def LogEvent(incomingData):
    timeNow = time.strftime('%H:%M:%S')
    dateNow = datetime.date.today()
    logEventFile = open('Log_Event1.txt','a')
    logEventFile.write('{} {} {}\r\n'.format(dateNow,timeNow,incomingData))
    logEventFile.close()
            
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
        CheckDistanceLimit(processedData[1])
    elif processedData[0] == 'AL1' or processedData[0] == 'AL2':
    	pass
    else:
        LogEvent(processedData)
        
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
    checkSerialStatusThread = threading.Thread(name='connectionStatusCheck',target=CheckSerialStatus, daemon=True)
    checkSerialStatusThread.start()
    ActivationThread = threading.Thread(name='AllActivationCheck',target=CheckAllActivation, daemon=True)
    ActivationThread.start()
    getSensorsThread = threading.Thread(name='sensorActivationCheck',target=GetDistanceSensors, daemon=True)
    getSensorsThread.start()
    fanActivationThread = threading.Thread(name='fanActivationCheck',target=CheckFanActivation, daemon=True)
    fanActivationThread.start()
    showTime = threading.Thread(name='timeCheck',target=DisplayTime, daemon=True)
    showTime.start()
    root.mainloop()

if __name__ == '__main__':
    main()