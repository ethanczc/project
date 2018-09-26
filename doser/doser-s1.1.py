from tkinter import *
import time
import threading
import datetime
import serial

root = Tk()
root.title('doser-s1.1 ')
root.geometry('')

# **************** time control start ***************

clockLabel = Label(root, text='clock',font=('times',16)).grid(row=0,column=0, padx=5,pady=5)
clock = Label(root, font=('times', 20, 'bold'), bg='white')
clock.grid(row=0,column=1,pady=5, padx=5)

config_Label = Label(root,text='Configuration').grid(row=1,column=0)
config_Entry = Entry(root)
config_Entry.grid(row=1,column=1) 

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
    global ecStage1Duration, ecStage2Duration, ecStage3Duration, daysPassed, currentStage
    if daysPassed <= ecStage1Duration:
        currentStage =1
    elif ecStage1Duration <= daysPassed <= (ecStage1Duration + ecStage2Duration):
        currentStage =2
    elif (ecStage1Duration + ecStage2Duration) <= daysPassed <= (ecStage1Duration + ecStage2Duration + ecStage3Duration):
        currentStage =3
    currentStageDisplay.config(text=currentStage)
    
daysPassed = 0

# **************** time control end ***************

# ********************** tank parameters start ***************

waterTankParameters_Label = Label(root,text='TANK PARAMETERS').grid(row=6,column=0,columnspan=2)

waterTankSize_Set = Label(root,text='Set Tank size (mL)').grid(row=7,column=0)
waterTankSize_Entry = Entry(root)
waterTankSize_Entry.grid(row=7,column=1)

waterTankSize_Label = Label(root,text='Tank Size (mL)').grid(row=8,column=0)
waterTankSize_Display = Label(root,text='')
waterTankSize_Display.grid(row=8,column=1)

waterTankSize = 0

def UpdateTankSize():
    global waterTankSize
    waterTankSize = int(waterTankSize_Entry.get())
    waterTankSize_Display.config(text='{} mL'.format(waterTankSize))
    print('Set Tank size: ' + str(waterTankSize) + ' mL ' + str(int(waterTankSize/1000)) + ' L' )

waterTankSize_Button = Button(root,text='Update Tank Size',command=UpdateTankSize)
waterTankSize_Button.grid(row=9,column=0,columnspan=2)

# ********************** tank parameters end ***************

# ********************* serial control start **********

serialControlLabel = Label(root,text='SERIAL CONTROL').grid(row=0,column=2,columnspan=2)

serialPort_Entry = Entry(root)
serialPort_Entry.grid(row=1,column=3)
serialPort_Entry.insert(END,'/dev/ttyUSB*')

ser = serial.Serial()
ser.baudrate = 9600

def SerialConnect():
    serialAddress = serialPort_Entry.get()
    ser.port = str(serialAddress)
    try:
        ser.open()
    except:
        serialStatus_Display.config(text='Failed to connect')
    else:
        serialStatus_Display.config(text=serialAddress)
        serialPort_Entry.config(state='disable')
        serialConnect_Button.config(state='disable')
        checkIncomingSerialThread = threading.Thread(target=CheckIncomingSerial, daemon=True)
        checkIncomingSerialThread.start()

serialConnect_Button = Button(root,text='Port connect',command = SerialConnect)
serialConnect_Button.grid(row=1,column=2)

serialStatus_Label = Label(root,text='Serial Port').grid(row=2,column=2)

serialStatus_Display = Label(root, text = 'Disconnected')
serialStatus_Display.grid(row=2, column=3)

serialEntry = Entry(root)
serialEntry.grid(row=3, column=3)

def SendSerial():
    try:
        message = serialEntry.get()
    except:
        pass
    else:
        pass
        ser.write(message.encode()) #encode message before sending to arduino

serialSend_Button = Button(root, text='send serial', command = SendSerial)
serialSend_Button.grid(row=3,column=2)

# ********************** serial control end ********************

# ********************** recipe control start ********************

recipeBlankSpace = Label(root,text='').grid(row=4,column=2,columnspan=2)

recipe_Label = Label(root,text='RECIPE CONTROL').grid(row=5,column=2,columnspan=2)

def LoadRecipe():
    recipeName = file_Entry.get()
    try:
        file=open(recipeName,'r')
    except:
        recipeName_Display.config(text='recipe not found')
    else:
        recipeContent = file.readlines()
        ReadRecipe(recipeContent)

fileLoad_Button = Button(root,text='Load recipe',command=LoadRecipe)
fileLoad_Button.grid(row=6,column=2)
file_Entry = Entry(root)
file_Entry.grid(row=6,column=3)
file_Entry.insert(END,'recipe_default.txt')

recipeName_Label = Label(root,text='Recipe Name').grid(row=7,column=2)
recipeName_Display = Label(root,text='')
recipeName_Display.grid(row=7,column=3)

def ReadRecipe(recipeContent):
    for line in range (0,len(recipeContent)):
        thisLine = recipeContent[line][:-1] # splice off \r\n
        thisLine = thisLine.split(' ') #split line into 2 items in an array
        parameter = thisLine[0] # allocate 1st item as parameter
        value = thisLine[1] # allocate 2nd items as value
        if parameter == 'recipe_name':
            recipeName_Display.config(text=value)
        if parameter == 'configuration':
            config_Entry.insert(END,value)
        if parameter == 'start_date':
            startDateEntry.insert(END,value)
        if parameter == 'tank_size':
            waterTankSize_Entry.insert(END,value)
        if parameter == 'water_check':
            waterCheck_Entry.insert(END,value)
        if parameter == 'ec_check':
            ecCheck_Entry.insert(END,value)
        if parameter == 'stage1_ec':
            ecStage1Target_Entry.insert(END,value)
        if parameter == 'stage1_duration':
            ecStage1Duration_Entry.insert(END,value)
        if parameter == 'stage2_ec':
            ecStage2Target_Entry.insert(END,value)
        if parameter == 'stage2_duration':
            ecStage2Duration_Entry.insert(END,value)
        if parameter == 'stage3_ec':
            ecStage3Target_Entry.insert(END,value)
        if parameter == 'stage3_duration':
            ecStage3Duration_Entry.insert(END,value)

# ********************** recipe control end **********************

# ********************** dosing control start *******************

blankSpace1Label = Label(root,text='* * * * * * * * * * * * * *').grid(row=12,column=0,columnspan=6)

dosingControlLabel = Label(root,text='DOSING CONTROL').grid(row=14,column=0,columnspan=2)

waterCheck_Label = Label(root,text='Water check timing').grid(row=15,column=0)
waterCheck_Entry = Entry(root)
waterCheck_Entry.grid(row=15,column=1)

ecCheck_Label = Label(root,text='EC check timing').grid(row=16,column=0)
ecCheck_Entry = Entry(root)
ecCheck_Entry.grid(row=16,column=1)

# STAGE 1
dosingStage1Label = Label(root,text='STAGE 1').grid(row=17,column=0,columnspan=2)

ecStage1Target_Label = Label(root,text='Stage 1 EC target').grid(row=18,column=0)
ecStage1Target_Entry = Entry(root)
ecStage1Target_Entry.grid(row=18,column=1)

ecStage1Duration_Label = Label(root,text='Stage 1 duration').grid(row=19,column=0)
ecStage1Duration_Entry = Entry(root)
ecStage1Duration_Entry.grid(row=19,column=1)
# STAGE 2
dosingStage2Label = Label(root,text='STAGE 2').grid(row=20,column=0,columnspan=2)

ecStage2Target_Label = Label(root,text='Stage 2 EC target').grid(row=21,column=0)
ecStage2Target_Entry = Entry(root)
ecStage2Target_Entry.grid(row=21,column=1)

ecStage2Duration_Label = Label(root,text='Stage 2 duration').grid(row=22,column=0)
ecStage2Duration_Entry = Entry(root)
ecStage2Duration_Entry.grid(row=22,column=1)
# STAGE 3
dosingStage3Label = Label(root,text='STAGE 3').grid(row=23,column=0,columnspan=2)

ecStage3Target_Label = Label(root,text='Stage 3 EC target').grid(row=24,column=0)
ecStage3Target_Entry = Entry(root)
ecStage3Target_Entry.grid(row=24,column=1)

ecStage3Duration_Label = Label(root,text='Stage 3 duration').grid(row=25,column=0)
ecStage3Duration_Entry = Entry(root)
ecStage3Duration_Entry.grid(row=25,column=1)

waterCheckTimings, ecCheckTimings = [] , []
ecStage1Target, ecStage2Target, ecStage3Target = 1.0, 1.0, 1.0
ecStage1Duration, ecStage2Duration, ecStage3Duration = 4, 6, 50

def UpdateDosingControl():
    global ecStage1Target, ecStage2Target, ecStage3Target
    global ecStage1Duration, ecStage2Duration, ecStage3Duration
    global waterCheckTimings, ecCheckTimings

    try:
        waterCheckTimings = waterCheck_Entry.get().split(',')
        ecCheckTimings = ecCheck_Entry.get().split(',')
        ecStage1Target = float(ecStage1Target_Entry.get())
        ecStage2Target = float(ecStage2Target_Entry.get())
        ecStage3Target = float(ecStage3Target_Entry.get())
        ecStage1Duration = int(ecStage1Duration_Entry.get())
        ecStage2Duration = int(ecStage2Duration_Entry.get())
        ecStage3Duration = int(ecStage3Duration_Entry.get())
    except:
        pass
    else:
        print(str(waterCheckTimings) + '\r\n' + str(ecCheckTimings) + '\r\nStage1: ' + str(ecStage1Target)\
         + '\r\nStage2: '+ str(ecStage2Target) + '\r\nStage3: ' + str(ecStage3Target))

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

# ********************** EC status start ***************

ECStatus_Label = Label(root,text='EC SENSOR').grid(row=14,column=2,columnspan=2)
ECCurrent_Label = Label(root,text='Current EC').grid(row=15,column=2)
ECCurrent_Display = Label(root,text='0')
ECCurrent_Display.grid(row=15,column=3)

temperature_Label = Label(root,text='Current Temp').grid(row=16,column=2)
temperature_Display = Label(root, text='0')
temperature_Display.grid(row=16,column=3)

# ********************** EC status end ***************

# ********************** checks & activation start ********************

def CheckActivation():
    global waterCheckTimings, ecCheckTimings, dosingAutoState
    while True:
        if dosingAutoState == True:
            timeNow = time.strftime('%H:%M:%S')
            for thisTime in waterCheckTimings:
                if thisTime == timeNow:
                    WaterPumpActivation(1)
            for thisTime in ecCheckTimings:
                if thisTime == timeNow:
                    EcCheck()
        time.sleep(1)

def WaterPumpActivation(state):
    ser.write(('PU {}'.format(state)).encode())

def EcCheck():
    ser.write(('AEC 1').encode())

def ECDose(ecValue): # triggered by 'AEC' from uno
    global waterTankSize, ecStage1Target, ecStage2Target, ecStage3Target, currentStage
    nutrientVolume = 0
    ECFactor = 100.0
    # uncomment below for de-bugging
    #ecValue = 0.5
    ECCurrent_Display.config(text=ecValue)
    if ecValue == 0 or ecValue == 100: # for out of range values, uno api sends a 0 or 100.
        nutrientVolume = 0
    elif currentStage == 1:
        nutrientVolume = (ecStage1Target - ecValue) * float(waterTankSize) / ECFactor
    elif currentStage == 2:
        nutrientVolume = (ecStage2Target - ecValue) * float(waterTankSize) / ECFactor
    elif currentStage == 3:
        nutrientVolume = (ecStage3Target - ecValue) * float(waterTankSize) / ECFactor
        
    nutrientVolume = int(round(nutrientVolume))
    if nutrientVolume <= 0:
        ser.write(('NP 0').encode())
    else:
        # must divide nutrientVolume by 2 as it is a total of 2 pumps
        ser.write(('NP {}'.format(nutrientVolume/2)).encode())

# ********************** checks & activation end ********************

# ********************** incoming serial start ********************

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
    if processedData[0] == 'EC': # only to get EC value
        ECCurrent_Display.config(text=processedData[1])
        
    if processedData[0] == 'AEC': # uses EC value to do automated dosing
        ECCurrent_Display.config(text=processedData[1])
        ECDose(processedData[1])
        
    if processedData[0] == 'TP':
    	temperature_Display.config(text=[processedData[1]])

# ********************** incoming serial end ********************

def main():
    displayTimeThread = threading.Thread(target=DisplayTime, daemon=True)
    displayTimeThread.start()
    checkActivationThread = threading.Thread(target=CheckActivation,daemon=True)
    checkActivationThread.start()
    root.mainloop()

if __name__ == '__main__':
    main()
