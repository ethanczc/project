from tkinter import*
import time
import threading
import serial
import datetime

root= Tk()
root.title('serial test')
root.geometry('800x700')

ser = serial.Serial('/dev/ttyUSB0',9600)

clockLabel = Label(root, text='clock',font=('times',16)).grid(row=0,column=0, padx=5,pady=5)
clock = Label(root, font=('times', 20, 'bold'), bg='white')
clock.grid(row=0,column=1,pady=5, padx=5)

currentDateLabel = Label(root,text='Current Date').grid(row=1,column=0)
currentDateDisplay = Label(root,text='1')
currentDateDisplay.grid(row=1,column=1)

serialControlLabel = Label(root,text='SERIAL CONTROL').grid(row=3,column=0,columnspan=2)

serialStatusLabel = Label(root, text='Serial Status').grid(row=4,column=0)
serialStatusDisplay = Label(root, text = 'Disconnected')
serialStatusDisplay.grid(row=4, column=1)

serialEntryLabel = Label(root, text='Serial Command').grid(row=5,column=0)
serialEntry = Entry(root)
serialEntry.grid(row=5, column=1)

def SendSerial():
    try:
        message = serialEntry.get()
    except:
        pass
    else:
        ser.write(message.encode()) #encode message before sending to arduino

serialSendButton = Button(root, text='send serial', command = SendSerial)
serialSendButton.grid(row=6,column=0,columnspan=2)

lightControlLabel = Label(root,text='LIGHTS CONTROL').grid(row=7,column=0,columnspan=2)

lightOnLabel = Label(root,text='Lights ON').grid(row=8,column=0)
lightOnEntry = Entry(root)
lightOnEntry.grid(row=8,column=1)

lightOffLabel = Label(root,text='Lights OFF').grid(row=9,column=0)
lightOffEntry = Entry(root)
lightOffEntry.grid(row=9,column=1)

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
UpdateLightButton.grid(row=10,column=0,columnspan=2)

lightAutoManualState = False

def ChangeLightAutoManualState():
    global lightAutoManualState
    lightAutoManualState = not lightAutoManualState
    if (lightAutoManualState == True):
        lightAutoManualStateDisplay.config(text='AUTO LIGHTS', fg= 'blue')
    else:
        lightAutoManualStateDisplay.config(text='MANUAL LIGHTS', fg='red')

lightAutoManualButton = Button(root, text = 'Auto/Manual Toggle', command=ChangeLightAutoManualState)
lightAutoManualButton.grid(row=11, column=0)

lightAutoManualStateDisplay = Label(root, text='MANUAL LIGHTS',fg='red')
lightAutoManualStateDisplay.grid(row=11, column=1)

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
        ser.write(('L1 1').encode())
    else:
        ser.write(('L1 0').encode())
        
def ManualLightToggle():
    global lightAutoManualState, lightState
    if lightAutoManualState == False:
        lightState = not lightState
        if lightState == True:
            LightActivation(True)
        else:
            LightActivation(False)

lightToggleLabel = Label(root,text='Manual Light On/Off Toggle').grid(row=12,column=0)
lightToggleButton = Button(root,text='TOGGLE',command=ManualLightToggle)
lightToggleButton.grid(row=12,column=1)

startDateLabel = Label(root,text='Start Date').grid(row=0, column=2)
startDateEntry = Entry(root)
startDateEntry.grid(row=0,column=3)

currentStageLabel = Label(root,text='Current Stage').grid(row=1,column=2)
currentStageDisplay = Label(root,text='1')
currentStageDisplay.grid(row=1,column=3)

daysPassedLabel = Label(root,text='Days Passed').grid(row=2,column=2)
daysPassedDisplay = Label(root,text='1')
daysPassedDisplay.grid(row=2,column=3)

sensorsLabel = Label(root,text='SENSORS').grid(row=3,column=2,columnspan=2)

temp1Label = Label(root, text = 'Temp1').grid(row=4,column=2)
temp1Display = Label(root, text= '')
temp1Display.grid(row=4, column=3)

temp2Label = Label(root, text = 'Temp2').grid(row=5,column=2)
temp2Display = Label(root, text= '')
temp2Display.grid(row=5, column=3)

tempAvgLabel = Label(root, text = 'A.Temp').grid(row=6,column=2)
tempAvgDisplay = Label(root, text= '')
tempAvgDisplay.grid(row=6, column=3)

tempIntervalLabel = Label(root, text='Temp interval (seconds)').grid(row=7,column=2)
tempIntervalEntry = Entry(root)
tempIntervalEntry.grid(row=7,column=3)

humidityLabel = Label(root, text = 'Humidity').grid(row=8,column=2)
humidityDisplay = Label(root,text='')
humidityDisplay.grid(row=8,column=3)

humdityIntervalLabel = Label(root, text='Humidity interval (mins)').grid(row=9,column=2)
humidityIntervalEntry = Entry(root)
humidityIntervalEntry.grid(row=9,column=3)

distanceDisplayLabel = Label(root, text = 'Waterlevel').grid(row=10,column=2)
distanceDisplay = Label(root,text='')
distanceDisplay.grid(row=10,column=3)

distanceIntervalLabel = Label(root, text='Waterlevel interval (mins)').grid(row=11,column=2)
distanceIntervalEntry = Entry(root)
distanceIntervalEntry.grid(row=11,column=3)

def UpdateTimeIntervals():
    try:
        tempInterval = tempIntervalEntry.get()
        humidityInterval = humidityIntervalEntry.get()
        distanceInterval = distanceIntervalEntry.get()
    except:
        pass
    else:
        ser.write(('T0 {}\r\n'.format(tempInterval)).encode())
        ser.write(('H0 {}\r\n'.format(humidityInterval)).encode())
        ser.write(('D0 {}'.format(distanceInterval)).encode())

updateIntervalsButton = Button(root, text = 'Update Time Intervals',command=UpdateTimeIntervals)
updateIntervalsButton.grid(row=12,column=2,columnspan=2)

# GUI for pump 1

pump1ControlLabel = Label(root,text='PUMP 1 CONTROL').grid(row=13,column=0,columnspan=2)

pump1Stage1_Label = Label(root,text='STAGE 1').grid(row=14,column=0,columnspan=2)

pump1Stage1_OnLabel = Label(root,text='Stage 1 ON').grid(row=15,column=0)
pump1Stage1_OnEntry = Entry(root)
pump1Stage1_OnEntry.grid(row=15,column=1)

pump1Stage1_OffLabel = Label(root,text='Stage 1 DRAIN').grid(row=16,column=0)
pump1Stage1_OffEntry = Entry(root)
pump1Stage1_OffEntry.grid(row=16,column=1)

pump1Stage1_DurationLabel = Label(root,text='Stage 1 Duration').grid(row=17,column=0)
pump1Stage1_DurationEntry = Entry(root)
pump1Stage1_DurationEntry.grid(row=17,column=1)

pump1Stage2_Label = Label(root,text='STAGE 2').grid(row=18,column=0,columnspan=2)

pump1Stage2_OnLabel = Label(root,text='Stage 2 ON').grid(row=19,column=0)
pump1Stage2_OnEntry = Entry(root)
pump1Stage2_OnEntry.grid(row=19,column=1)

pump1Stage2_OffLabel = Label(root,text='Stage 2 DRAIN').grid(row=20,column=0)
pump1Stage2_OffEntry = Entry(root)
pump1Stage2_OffEntry.grid(row=20,column=1)

pump1Stage2_DurationLabel = Label(root,text='Stage 2 Duration').grid(row=21,column=0)
pump1Stage2_DurationEntry = Entry(root)
pump1Stage2_DurationEntry.grid(row=21,column=1)

pump1Stage2_Label = Label(root,text='STAGE 3').grid(row=22,column=0,columnspan=2)

pump1Stage3_OnLabel = Label(root,text='Stage 3 ON').grid(row=23,column=0)
pump1Stage3_OnEntry = Entry(root)
pump1Stage3_OnEntry.grid(row=23,column=1)

pump1Stage3_OffLabel = Label(root,text='Stage 3 DRAIN').grid(row=24,column=0)
pump1Stage3_OffEntry = Entry(root)
pump1Stage3_OffEntry.grid(row=24,column=1)

pump1Stage3_DurationLabel = Label(root,text='Stage 3 Duration').grid(row=25,column=0)
pump1Stage3_DurationEntry = Entry(root)
pump1Stage3_DurationEntry.grid(row=25,column=1)

pump1Drain_DurationLabel = Label(root,text='Drain Duration').grid(row=26,column=0)
pump1Drain_DurationEntry = Entry(root)
pump1Drain_DurationEntry.grid(row=26,column=1)

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
    
    print(pump1Stage1_OnTimings)
    print(pump1Stage1_OffTimings)
    print(pump1Stage2_OnTimings)
    print(pump1Stage2_OffTimings)
    print(pump1Stage3_OnTimings)
    print(pump1Stage3_OffTimings)

UpdatePumpButton = Button(root, text='Update Pump Parameters',command=UpdatePump1Timings)
UpdatePumpButton.grid(row=27,column=0,columnspan=2)

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
                        PumpActivation(True)
                for thisTime in pump1Stage1_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(True)
            elif currentStage == 2:
                for thisTime in pump1Stage2_OnTimings:
                    if thisTime == timeNow:
                        PumpActivation(True)
                for thisTime in pump1Stage2_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(True)
            elif currentStage == 3:
                for thisTime in pump1Stage3_OnTimings:
                    if thisTime == timeNow:
                        PumpActivation(True)
                for thisTime in pump1Stage3_OffTimings:
                    if thisTime == timeNow:
                        DrainActivation(True)
        time.sleep(1)
        
def PumpActivation(state):

    if state == True:
        ser.write(('P1 1').encode())
    else:
        ser.write(('P1 0').encode())
        
def DrainActivation(state):
    pass
        
def ChangePumpAutoManualState():
    global pumpAutoManualState
    pumpAutoManualState = not pumpAutoManualState
    if (pumpAutoManualState == True):
        pumpAutoManualStateDisplay.config(text='AUTO PUMP 1', fg= 'blue')
    else:
        pumpAutoManualStateDisplay.config(text='MANUAL PUMP 1', fg='red')

pumpAutoManualButton = Button(root, text = 'Auto/Manual Toggle', command=ChangePumpAutoManualState)
pumpAutoManualButton.grid(row=28, column=0)

pumpAutoManualStateDisplay = Label(root, text='MANUAL PUMP 1',fg='red')
pumpAutoManualStateDisplay.grid(row=28, column=1)
    
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
        except:
            pass
        else:
            rawDataList = rawData.split(' ')
            command = rawDataList[0]
            value = float(rawDataList[1])
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
        
    if processedData[0] == 'T1' or processedData[0] == 'T2': 
        TemperatureFunction(processedData[0],processedData[1])
    elif processedData[0] == 'H1':
        humidityDisplay.config(text = processedData[1])   
    elif processedData[0] == 'D1':
        distanceDisplay.config(text = processedData[1])
        
temp1 = 0
temp2 = 0

def TemperatureFunction(sensor,temperature):
    global temp1, temp2
    if sensor == 'T1':
        temp1Display.config(text=temperature)
        temp1 = temperature
    elif sensor == 'T2':
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
    showTime = threading.Thread(name='serialCheck',target=DisplayTime, daemon=True)
    showTime.start()
    root.mainloop()

if __name__ == '__main__':
    main()