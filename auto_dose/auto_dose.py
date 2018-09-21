from tkinter import *
import time
import threading
import datetime
#import serial

root = Tk()
root.title('auto dose program')
root.geometry('700x600')

# **************** time control start ***************

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

def DisplayTime():
    while True:
        timeNow = time.strftime('%H:%M:%S')
        dateNow = time.strftime('%d/%m/%y')
        clock.config(text=timeNow)
        currentDateDisplay.config(text=dateNow)
        DisplayDaysPassed()
        DisplayCurrentStage()
        time.sleep(1)

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
    
currentStage = 1

def DisplayCurrentStage():
    global ecStage1Duration, ecStage2Duration, ecStage3Duration, daysPassed
    if daysPassed <= ecStage1Duration:
        currentStage =1
    elif ecStage1Duration <= daysPassed <= (ecStage1Duration + ecStage2Duration):
        currentStage =2
    elif (ecStage1Duration + ecStage2Duration) <= daysPassed <= (ecStage1Duration + ecStage2Duration + ecStage3Duration):
        currentStage =3
    currentStageDisplay.config(text=currentStage)
    
daysPassed = 0

# **************** time control end ***************

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
        pass
        #ser.write(message.encode()) #encode message before sending to arduino

serialSendButton = Button(root, text='send serial', command = SendSerial)
serialSendButton.grid(row=11,column=0,columnspan=2)

blankSpace1Label = Label(root,text='').grid(row=12,column=0,columnspan=6)

# ********************** serial control end ********************

# ********************** dosing control start *******************

dosingControlLabel = Label(root,text='DOSING CONTROL').grid(row=14,column=0,columnspan=2)

waterCheck_Label = Label(root,text='Water check timing').grid(row=15,column=0)
waterCheck_Entry = Entry(root)
waterCheck_Entry.insert(END, '21:00:00')
waterCheck_Entry.grid(row=15,column=1)

ecCheck_Label = Label(root,text='EC check timing').grid(row=16,column=0)
ecCheck_Entry = Entry(root)
ecCheck_Entry.insert(END, '21:30:00')
ecCheck_Entry.grid(row=16,column=1)

# STAGE 1
dosingStage1Label = Label(root,text='STAGE 1').grid(row=17,column=0,columnspan=2)

ecStage1Target_Label = Label(root,text='Stage 1 EC target').grid(row=18,column=0)
ecStage1Target_Entry = Entry(root)
ecStage1Target_Entry.insert(END,'0.5')
ecStage1Target_Entry.grid(row=18,column=1)

ecStage1Duration_Label = Label(root,text='Stage 1 duration').grid(row=19,column=0)
ecStage1Duration_Entry = Entry(root)
ecStage1Duration_Entry.insert(END, '4')
ecStage1Duration_Entry.grid(row=19,column=1)
# STAGE 2
dosingStage2Label = Label(root,text='STAGE 2').grid(row=20,column=0,columnspan=2)

ecStage2Target_Label = Label(root,text='Stage 2 EC target').grid(row=21,column=0)
ecStage2Target_Entry = Entry(root)
ecStage2Target_Entry.insert(END,'1.1')
ecStage2Target_Entry.grid(row=21,column=1)

ecStage2Duration_Label = Label(root,text='Stage 2 duration').grid(row=22,column=0)
ecStage2Duration_Entry = Entry(root)
ecStage2Duration_Entry.insert(END, '6')
ecStage2Duration_Entry.grid(row=22,column=1)
# STAGE 3
dosingStage3Label = Label(root,text='STAGE 3').grid(row=23,column=0,columnspan=2)

ecStage3Target_Label = Label(root,text='Stage 3 EC target').grid(row=24,column=0)
ecStage3Target_Entry = Entry(root)
ecStage3Target_Entry.insert(END,'1.4')
ecStage3Target_Entry.grid(row=24,column=1)

ecStage3Duration_Label = Label(root,text='Stage 3 duration').grid(row=25,column=0)
ecStage3Duration_Entry = Entry(root)
ecStage3Duration_Entry.insert(END, '40')
ecStage3Duration_Entry.grid(row=25,column=1)

waterCheckTimings, ecCheckTimings = [] , []
ecStage1Target, ecStage2Target, ecStage3Target = 0.5, 1.1, 1.4
ecStage1Duration, ecStage2Duration, ecStage3Duration = 4, 6, 40

def UpdateDosingControl():
    global ecStage1Target, ecStage2Target, ecStage3Target
    global ecStage1Duration, ecStage2Duration, ecStage3Duration

    try:
        waterCheckTimings = waterCheck_Entry.get().split(' , ')
        ecCheckTimings = ecCheck_Entry.get().split(' , ')
        ecStage1Target = float(ecStage1Target_Entry.get())
        ecStage2Target = float(ecStage2Target_Entry.get())
        ecStage3Target = float(ecStage3Target_Entry.get())
        ecStage1Duration = int(ecStage1Duration_Entry.get())
        ecStage2Duration = int(ecStage2Duration_Entry.get())
        ecStage3Duration = int(ecStage3Duration_Entry.get())
    except:
        pass
    else:
        print(str(waterCheckTimings) + '\r\n' + str(ecCheckTimings) + '\r\n' + str(ecStage1Target) + '\r\n'\
         + str(ecStage2Target) + '\r\n' + str(ecStage3Target))

updateDosingControl_Button = Button(root,text='Update Dosing Control',command=UpdateDosingControl)
updateDosingControl_Button.grid(row=28,column=0,columnspan=2)

dosingAutoState = False

def ChangeDosingAutoState():
    global dosingAutoState
    dosingAutoState = not dosingAutoState
    if (dosingAutoState):
        dosingAutoState_Display.config(text='AUTO DOSING',fg='blue')
    else:
        dosingAutoState_Display.config(text='MANUAL DOSING',fg='red')

dosingAutoState_Button = Button(root,text='CHANGE MODE',command=ChangeDosingAutoState)
dosingAutoState_Button.grid(row=29,column=0)

dosingAutoState_Display = Label(root,text='MANUAL DOSING',fg='red')
dosingAutoState_Display.grid(row=29,column=1)

# ********************** dosing control end ********************

# ********************** checks & activation start ********************

def CheckActivation():
    global waterCheckTimings, ecCheckTimings
    while True:
        if dosingAutoState:
            timeNow = time.strftime('%H:%M:%S')
            for thisTime in waterCheckTimings:
                if thisTime == timeNow:
                    WaterPumpActivation(1)
            for thisTime in ecCheckTimings:
                if thisTime == timeNow:
                    EcCheck()

def WaterPumpActivation(state):
    pass
    #ser.write(('PU {}'.format(state)).encode())

def EcCheck(state):
    pass
    #ser.write(('AEC 1').encode())

def EcDose(ecValue):
    global waterTankSize, ecStage1Target, ecStage2Target, ecStage3Target, currentStage
    volDifference = 0
    if currentStage == 1:
        volDifference = (ecStage1Target - ecValue) * 100
    elif currentStage == 2:
        volDifference = (ecStage2Target - ecValue) * 100
    elif currentStage ==3:
        volDifference = (ecStage3Target - ecValue) * 100
    if volDifference >= 10:
        duration = volDifference * 400
    ser.write(('NP {}'.format(duration)).encode())

# ********************** checks & activation end ********************

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

lightAutoManualButton = Button(root, text = 'CHANGE MODE', command=ChangeLightAutoManualState)
lightAutoManualButton.grid(row=4, column=2)

lightAutoManualStateDisplay = Label(root, text='MANUAL LIGHTS',fg='red')
lightAutoManualStateDisplay.grid(row=4, column=3)

lightState = False

def LightActivation(state):

    if state == True:
        ser.write(('LT1 1').encode())
    else:
        ser.write(('LT1 0').encode())

# ********************** light control end *******************

# ********************** tank parameters start ***************

waterTankParameters_Label = Label(root,text='TANK PARAMETERS').grid(row=8,column=2,columnspan=2)
waterTankSize_Set = Label(root,text='Set Tank size').grid(row=9,column=2)
waterTankSize_Entry = Entry(root)
waterTankSize_Entry.grid(row=9,column=3)

waterTankSize_Label = Label(root,text='Tank Size').grid(row=10,column=2)
waterTankSize_Display = Label(root,text='')
waterTankSize_Display.grid(row=10,column=3)

waterTankSize = 0

def UpdateTankSize():
    waterTankSize = int(waterTankSize_Entry.get())
    waterTankSize_Display.config(text=waterTankSize)
    print(waterTankSize)

waterTankSize_Button = Button(root,text='Update Tank Size',command=UpdateTankSize)
waterTankSize_Button.grid(row=11,column=2,columnspan=2)

# ********************** tank parameters end ***************

ECStatus_Label = Label(root,text='EC SENSOR').grid(row=14,column=2,columnspan=2)
ECCurrent_Label = Label(root,text='Current EC').grid(row=15,column=2)
ECCurrent_Display = Label(root,text='0')
ECCurrent_Display.grid(row=15,column=3)

temperature_Label = Label(root,text='Current Temp').grid(row=16,column=2)
temperature_Display = Label(root, text='0')
temperature_Display.grid(row=16,column=3)

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
            CheckData(processedData)
            print(processedData)

def CheckData(processedData):
    if processedData[0] == 'EC':
        ECCurrent_Display.config(text=processedData[1])
    if processedData[0] == 'AEC':
        ECDose(processedData[1])
    if processedData[0] == 'TP':
    	temperature_Display.config(text=[processedData[1]])

def main():
    root.mainloop()

if __name__ == '__main__':
    checkIncomingSerialThread = threading.Thread(target=CheckIncomingSerial, daemon=True)
    checkIncomingSerialThread.start()
    displayTimeThread = threading.Thread(target=DisplayTime, daemon=True)
    displayTimeThread.start()
    checkActivationThread = threading.Thread(target=CheckActivation,daemon=True)
    checkActivationThread.start()
    main()
