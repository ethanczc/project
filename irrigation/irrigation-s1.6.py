from tkinter import*
import time
import threading
import serial
import datetime
import smtplib

root= Tk()
root.title('Irrigation Serial v1.6')
root.geometry('')

targetEmail = 'ethanczc@gmail.com'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ethanczc.rpi@gmail.com','zaq1@wsx')

# **************** time block start ***************

clock_Label = Label(root, text='CLOCK',font=('times',16)).grid(row=0,column=0, padx=5,pady=5)
clock = Label(root, font=('times', 20, 'bold'), bg='white')
clock.grid(row=0,column=1,pady=5, padx=5)

configLabel = Label (root,text='Configuration:').grid(row=1,column=0)
configEntry = Entry(root)
configEntry.grid(row=1,column=1)

currentDateLabel = Label(root,text='Current Date').grid(row=2,column=0)
currentDateDisplay = Label(root,text='1')
currentDateDisplay.grid(row=2,column=1)

startDateLabel = Label(root,text='Start Date').grid(row=3, column=0)
startDateEntry = Entry(root)
startDateEntry.grid(row=3,column=1)

daysPassedLabel = Label(root,text='Days Passed').grid(row=4,column=0)
daysPassedDisplay = Label(root,text='1',)
daysPassedDisplay.grid(row=4,column=1)

currentStageLabel = Label(root,text='Current Stage').grid(row=5,column=0)
currentStageDisplay = Label(root,text='1',font=('times', 12, 'bold'), bg='black', fg='white')
currentStageDisplay.grid(row=5,column=1)

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

ser = serial.Serial() # create serial object without port address first
ser.baudrate = 9600 

serialControlLabel = Label(root,text='SERIAL CONTROL').grid(row=7,column=0,columnspan=2)

def SerialConnect():
    serialAddress = serialPort_Entry.get()
    ser.port = str(serialAddress) #define serial port address here
    try:
        ser.open() #open serial port
    except:
        serialStatus_Display.config(text='failed to connect')
    else:
        serialStatus_Display.config(text=serialAddress)
        serialPort_Entry.config(state='disable')
        serialConnect_Button.config(state='disable')
        checkIncomingSerial_Thread = threading.Thread(target=CheckIncomingSerial,daemon=True)
        checkIncomingSerial_Thread.start()

serialConnect_Button = Button(root,text='Port Connect',command=SerialConnect)
serialConnect_Button.grid(row=8,column=0)

serialPort_Entry = Entry(root)
serialPort_Entry.grid(row=8,column=1)
serialPort_Entry.insert(END,'/dev/ttyUSB*')

serialStatus_Label = Label(root, text='Serial Status').grid(row=9,column=0)
serialStatus_Display = Label(root, text = 'Disconnected')
serialStatus_Display.grid(row=9, column=1)

serialEntry = Entry(root)
serialEntry.grid(row=10, column=1)

def SendSerial():
    message = serialEntry.get()
    if message == '':
        print ('no message') # check for empty message first
    else:
        try:
            ser.write(message.encode())
        except:
            print('unable to send serial data')
            
serialSendButton = Button(root, text='send serial', command = SendSerial)
serialSendButton.grid(row=10,column=0)

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
    try:
        lightOnTimings = (lightOnEntry.get()).split(',')
        lightOffTimings = (lightOffEntry.get()).split(',')
    except:
        pass
    else:
        print(str(lightOnTimings) + '\r\n' + str(lightOffTimings))
    
UpdateLightButton = Button(root, text='Update Light Timings',command=UpdateLightTimings)
UpdateLightButton.grid(row=3,column=2,columnspan=2)

lightAutoState = False

def ChangeLightAutoState():
    global lightAutoState
    lightAutoState = not lightAutoState
    if (lightAutoState == True):
        lightAutoStateDisplay.config(text='AUTO LIGHTS', fg= 'blue')
    else:
        lightAutoStateDisplay.config(text='MANUAL LIGHTS', fg='red')

lightAutoButton = Button(root, text = 'Auto Lights Toggle', command=ChangeLightAutoState)
lightAutoButton.grid(row=4, column=2)

lightAutoStateDisplay = Label(root, text='MANUAL LIGHTS',fg='red')
lightAutoStateDisplay.grid(row=4, column=3)

lightState = False

def LightActivation(state):

    if state == True:
        ser.write(('LT1 1').encode())
    else:
        ser.write(('LT1 0').encode())

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
distanceTimingEntry.insert(END,'06:01:00')
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
        distanceTiming = (distanceTimingEntry.get()).split(',')
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

# *********************** logging control start *********************

loggingBlankSpace = Label (root,text='').grid(row=12,column=4,rowspan=2,columnspan=2)

logging_Label = Label(root,text='LOGGING CONTROL').grid(row=14,column=4,columnspan=2)

def LogEvent(incomingData):
    global logAutoState
    if (logAutoState):
        timeNow = time.strftime('%H:%M:%S')
        dateNow = datetime.date.today()
        logAddress = logAddress_Entry.get()
        logEventFile = open(logAddress,'a')
        logEventFile.write('{} {} {}\r\n'.format(dateNow,timeNow,incomingData))
        logEventFile.close()

logAddress_Label = Label(root,text='Log File').grid(row=15,column=4)
logAddress_Entry = Entry(root)
logAddress_Entry.grid(row=15,column=5)
logAddress_Entry.insert(END,'Log_Default.txt')

logAutoState = False

def ChangeAutoLog():
    global logAutoState
    logAutoState = not logAutoState
    if (logAutoState):
        autologAutoState_Display.config(text='Logging',fg='blue')
    else:
        autologAutoState_Display.config(text='Not Logging',fg='red')

autoLog_Button = Button(root,text='Auto Log Toggle',command=ChangeAutoLog)
autoLog_Button.grid(row=16,column=4)
autologAutoState_Display = Label(root,text='Not Logging',fg='red')
autologAutoState_Display.grid(row=16,column=5)

# *********************** logging control end *********************

# *********************** recipe control start *********************

RecipeBlankSpace = Label(root,text='').grid(row=17,column=4,columnspan=2)
recipe_Label = Label(root,text='RECIPE CONTROL').grid(row=18,column=4, columnspan=2)

recipeContent = ''
def LoadRecipe():
    global recipeContent
    recipeName = file_Entry.get()
    try:
        file=open(recipeName,'r')
    except:
        recipeName_Display.config(text='recipe not found')
    else:
        recipeContent = file.readlines()
        ReadRecipe()

fileLoad_Button = Button(root,text='Load recipe',command=LoadRecipe)
fileLoad_Button.grid(row=19,column=4)
file_Entry = Entry(root)
file_Entry.grid(row=19,column=5)
file_Entry.insert(END,'recipe_default.txt')

recipeName_Label = Label(root,text='Recipe Name').grid(row=20,column=4)
recipeName_Display = Label(root,text='')
recipeName_Display.grid(row=20,column=5)

def ReadRecipe():
    global recipeContent
    for line in range (0,len(recipeContent)):
        thisLine = recipeContent[line][:-1] # splice off \r\n
        thisLine = thisLine.split(' ') #split line into 2 items in an array
        parameter = thisLine[0] # allocate 1st item as parameter
        value = thisLine[1] # allocate 2nd items as value
        if parameter == 'recipe_name':
            recipeName_Display.config(text=value)
        if parameter == 'configuration':
            configEntry.insert(END,value)
        if parameter == 'start_date':
            startDateEntry.insert(END,value)
        if parameter == 'light_on':
            lightOnEntry.insert(END,value)
        if parameter == 'light_off':
            lightOffEntry.insert(END,value)
        if parameter == 'pump1_stage1_on':
            pump1Stage1_On_Entry.insert(END,value)
        if parameter == 'pump1_stage1_drain':
            pump1Stage1_Drain_Entry.insert(END,value)
        if parameter == 'pump1_stage2_on':
            pump1Stage2_On_Entry.insert(END,value)
        if parameter == 'pump1_stage2_drain':
            pump1Stage2_Drain_Entry.insert(END,value)
        if parameter == 'pump1_stage3_on':
            pump1Stage3_On_Entry.insert(END,value)
        if parameter == 'pump1_stage3_drain':
            pump1Stage3_Drain_Entry.insert(END,value)
        if parameter == 'stage1_duration':
            stage1_Duration_Entry.insert(END,value)
        if parameter == 'stage2_duration':
            stage2_Duration_Entry.insert(END,value)
        if parameter == 'stage3_duration':
            stage3_Duration_Entry.insert(END,value)
        if parameter == 'drain_duration':
            drain_Duration_Entry.insert(END,value)
        if parameter == 'pump2_stage1_on':
            pump2Stage1_On_Entry.insert(END,value)
        if parameter == 'pump2_stage1_drain':
            pump2Stage1_Drain_Entry.insert(END,value)
        if parameter == 'pump2_stage2_on':
            pump2Stage2_On_Entry.insert(END,value)
        if parameter == 'pump2_stage2_drain':
            pump2Stage2_Drain_Entry.insert(END,value)
        if parameter == 'pump2_stage3_on':
            pump2Stage3_On_Entry.insert(END,value)
        if parameter == 'pump2_stage3_drain':
            pump2Stage3_Drain_Entry.insert(END,value)

# *********************** recipe control end ***********************

# *********************** pump 1 control start *******************

pump1Control_Label = Label(root,text='PUMP 1 CONTROL').grid(row=14,column=0,columnspan=2)

pump1Stage1_Label = Label(root,text='STAGE 1').grid(row=15,column=0,columnspan=2)

pump1Stage1_On_Label = Label(root,text='Stage 1 ON').grid(row=16,column=0)
pump1Stage1_On_Entry = Entry(root)
pump1Stage1_On_Entry.grid(row=16,column=1)

pump1Stage1_Drain_Label = Label(root,text='Stage 1 DRAIN').grid(row=17,column=0)
pump1Stage1_Drain_Entry = Entry(root)
pump1Stage1_Drain_Entry.grid(row=17,column=1)

stage1_Duration_Label = Label(root,text='Stage 1 Duration').grid(row=18,column=0)
stage1_Duration_Entry = Entry(root)
stage1_Duration_Entry.grid(row=18,column=1)

pump1Stage2_Label = Label(root,text='STAGE 2').grid(row=19,column=0,columnspan=2)

pump1Stage2_On_Label = Label(root,text='Stage 2 ON').grid(row=20,column=0)
pump1Stage2_On_Entry = Entry(root)
pump1Stage2_On_Entry.grid(row=20,column=1)

pump1Stage2_Drain_Label = Label(root,text='Stage 2 DRAIN').grid(row=21,column=0)
pump1Stage2_Drain_Entry = Entry(root)
pump1Stage2_Drain_Entry.grid(row=21,column=1)

stage2_Duration_Label = Label(root,text='Stage 2 Duration').grid(row=22,column=0)
stage2_Duration_Entry = Entry(root)
stage2_Duration_Entry.grid(row=22,column=1)

pump1Stage2_Label = Label(root,text='STAGE 3').grid(row=23,column=0,columnspan=2)

pump1Stage3_On_Label = Label(root,text='Stage 3 ON').grid(row=24,column=0)
pump1Stage3_On_Entry = Entry(root)
pump1Stage3_On_Entry.grid(row=24,column=1)

pump1Stage3_Drain_Label = Label(root,text='Stage 3 DRAIN').grid(row=25,column=0)
pump1Stage3_Drain_Entry = Entry(root)
pump1Stage3_Drain_Entry.grid(row=25,column=1)

stage3_Duration_Label = Label(root,text='Stage 3 Duration').grid(row=26,column=0)
stage3_Duration_Entry = Entry(root)
stage3_Duration_Entry.grid(row=26,column=1)

drain_Duration_Label = Label(root,text='Drain Duration').grid(row=27,column=0)
drain_Duration_Entry = Entry(root)
drain_Duration_Entry.grid(row=27,column=1)

pump1Stage1_OnTimings, pump1Stage1_OffTimings = [] , []
pump1Stage2_OnTimings, pump1Stage2_OffTimings = [] , []
pump1Stage3_OnTimings, pump1Stage3_OffTimings = [] , []
pump1Stage1_Duration, pump1Stage2_Duration = 0 , 0
pump1Stage3_Duration, pump1Drain_Duration = 0 , 0

def UpdatePump1Timings():
    global pump1Stage1_OnTimings, pump1Stage1_OffTimings, pump1Stage2_OnTimings, pump1Stage2_OffTimings, pump1Stage3_OnTimings, pump1Stage3_OffTimings
    global pump1Stage1_Duration,pump1Stage2_Duration,pump1Stage3_Duration, pump1Drain_Duration
    
    try:
        pump1Stage1_OnTimings = (pump1Stage1_On_Entry.get()).split(',')
        pump1Stage1_OffTimings= (pump1Stage1_Drain_Entry.get()).split(',')
        
        pump1Stage2_OnTimings = (pump1Stage2_On_Entry.get()).split(',')
        pump1Stage2_OffTimings= (pump1Stage2_Drain_Entry.get()).split(',')
        
        pump1Stage3_OnTimings = (pump1Stage3_On_Entry.get()).split(',')
        pump1Stage3_OffTimings= (pump1Stage3_Drain_Entry.get()).split(',')
        
        pump1Stage1_Duration = int(stage1_Duration_Entry.get())
        pump1Stage2_Duration = int(stage2_Duration_Entry.get())
        pump1Stage3_Duration = int(stage3_Duration_Entry.get())
        
        pump1Drain_Duration = int(drain_Duration_Entry.get())
        ser.write(('DR0 {}'.format(pump1Drain_Duration)).encode())
    except:
        print ('cannot send drain data via serial')
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

def ChangePump1AutoState():
    global pump1AutoState
    pump1AutoState = not pump1AutoState
    if (pump1AutoState == True):
        pump1AutoStateDisplay.config(text='AUTO PUMP 1', fg= 'blue')
    else:
        pump1AutoStateDisplay.config(text='MANUAL PUMP 1', fg='red')

pump1AutoButton = Button(root, text = 'Auto Pump 1 Toggle', command=ChangePump1AutoState)
pump1AutoButton.grid(row=29, column=0)

pump1AutoStateDisplay = Label(root, text='MANUAL PUMP 1',fg='red')
pump1AutoStateDisplay.grid(row=29, column=1)

pump1AutoState = False

#  ******************************** pump 1 control end *********************

#  ******************************** pump 2 control start *********************

pump2Control_Label = Label(root,text='PUMP 2 CONTROL').grid(row=14,column=2,columnspan=2)

pump2Stage1_Label = Label(root,text='STAGE 1').grid(row=15,column=2,columnspan=2)

pump2Stage1_On_Label = Label(root,text='Stage 1 ON').grid(row=16,column=2)
pump2Stage1_On_Entry = Entry(root)
pump2Stage1_On_Entry.grid(row=16,column=3)

pump2Stage1_Drain_Label = Label(root,text='Stage 1 DRAIN').grid(row=17,column=2)
pump2Stage1_Drain_Entry = Entry(root)
pump2Stage1_Drain_Entry.grid(row=17,column=3)

pump2Stage2_Label = Label(root,text='STAGE 2').grid(row=19,column=2,columnspan=2)

pump2Stage2_On_Label = Label(root,text='Stage 2 ON').grid(row=20,column=2)
pump2Stage2_On_Entry = Entry(root)
pump2Stage2_On_Entry.grid(row=20,column=3)

pump2Stage2_Drain_Label = Label(root,text='Stage 2 DRAIN').grid(row=21,column=2)
pump2Stage2_Drain_Entry = Entry(root)
pump2Stage2_Drain_Entry.grid(row=21,column=3)

pump2Stage2_Label = Label(root,text='STAGE 3').grid(row=23,column=2,columnspan=2)

pump2Stage3_On_Label = Label(root,text='Stage 3 ON').grid(row=24,column=2)
pump2Stage3_On_Entry = Entry(root)
pump2Stage3_On_Entry.grid(row=24,column=3)

pump2Stage3_Drain_Label = Label(root,text='Stage 3 DRAIN').grid(row=25,column=2)
pump2Stage3_Drain_Entry = Entry(root)
pump2Stage3_Drain_Entry.grid(row=25,column=3)

pump2Stage1_OnTimings, pump2Stage1_OffTimings = [] , []
pump2Stage2_OnTimings, pump2Stage2_OffTimings = [] , []
pump2Stage3_OnTimings, pump2Stage3_OffTimings = [] , []

def UpdatePump2Timings():
    global pump2Stage1_OnTimings, pump2Stage1_OffTimings, pump2Stage2_OnTimings, pump2Stage2_OffTimings, pump2Stage3_OnTimings, pump2Stage3_OffTimings
    try:
        pump2Stage1_OnTimings = (pump2Stage1_On_Entry.get()).split(',')
        pump2Stage1_OffTimings= (pump2Stage1_Drain_Entry.get()).split(',')
        
        pump2Stage2_OnTimings = (pump2Stage2_On_Entry.get()).split(',')
        pump2Stage2_OffTimings= (pump2Stage2_Drain_Entry.get()).split(',')
        
        pump2Stage3_OnTimings = (pump2Stage3_On_Entry.get()).split(',')
        pump2Stage3_OffTimings= (pump2Stage3_Drain_Entry.get()).split(',')

    except:
        pass
    else:
        print(pump2Stage1_OnTimings)
        print(pump2Stage1_OffTimings)
        print(pump2Stage2_OnTimings)
        print(pump2Stage2_OffTimings)
        print(pump2Stage3_OnTimings)
        print(pump2Stage3_OffTimings)
    
UpdatePump2Button = Button(root, text='Update Pump 2 Parameters',command=UpdatePump2Timings)
UpdatePump2Button.grid(row=28,column=2,columnspan=2)

def ChangePump2AutoState():
    global pump2AutoState
    pump2AutoState = not pump2AutoState
    if (pump2AutoState == True):
        pump2AutoStateDisplay.config(text='AUTO PUMP 2', fg= 'blue')
    else:
        pump2AutoStateDisplay.config(text='MANUAL PUMP 2', fg='red')

pump2AutoButton = Button(root, text = 'Auto Pump 2 Toggle', command=ChangePump2AutoState)
pump2AutoButton.grid(row=29, column=2)

pump2AutoStateDisplay = Label(root, text='MANUAL PUMP 2',fg='red')
pump2AutoStateDisplay.grid(row=29, column=3)

pump2AutoState = False

#  ******************************** pump 2 control end *********************

#  ******************************** pump and light general control start *********************

def CheckAllActivation():
    global pump1AutoState, pump1Stage1_OnTimings, pump1Stage1_OffTimings, pump1Stage2_OnTimings, pump1Stage2_OffTimings, pump1Stage3_OnTimings, pump1Stage3_OffTimings
    global pump2AutoState, pump2Stage1_OnTimings, pump2Stage1_OffTimings, pump2Stage2_OnTimings, pump2Stage2_OffTimings, pump2Stage3_OnTimings, pump2Stage3_OffTimings
    global lightAutoState, lightOnTimings, lightOffTimings, lightState
    while True:
        if pump1AutoState == True or pump2AutoState == True:
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

        if lightAutoState == True:
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
