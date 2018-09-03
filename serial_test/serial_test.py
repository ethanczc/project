from tkinter import*
import time
import threading
import serial

root= Tk()
root.title('serial test')
root.geometry('400x200')

ser = serial.Serial('/dev/ttyUSB0',9600)
    
def SendSerial():
    message = serialEntry.get()
    ser.write(message.encode()) #encode message before sending to arduino

serialStatusLabel = Label(root, text='Serial Status').grid(row=2,column=0)
serialStatus = Label(root, text = 'Disconnected')
serialStatus.grid(row=2, column=1)

serialEntryLabel = Label(root, text='Serial Command').grid(row=3,column=0)
serialEntry = Entry(root)
serialEntry.grid(row=3, column=1)
serialSendButton = Button(root, text='send serial', command = SendSerial)
serialSendButton.grid(row=4,column=0,columnspan=2)

tempDisplayLabel = Label(root, text = 'Temp').grid(row=5,column=0)
tempDisplay = Label(root, text= '')
tempDisplay.grid(row=5, column=1)

humidityDisplayLabel = Label(root, text = 'Humidity').grid(row=6,column=0)
humidityDisplay = Label(root,text='')
humidityDisplay.grid(row=6,column=1)

distanceDisplayLabel = Label(root, text = 'Distance').grid(row=7,column=0)
distanceDisplay = Label(root,text='')
distanceDisplay.grid(row=7,column=1)

def CheckIncomingSerial():
    while True:
        try:
            rawData = ser.readline()
            rawData = rawData.decode('utf-8') #decode message from arduino
            rawData = rawData[:-2] #splice off \r\n
            print('raw data received is {}'.format(rawData)) 
        except:
            serialStatus.config(text='Disconnected')
        else:
            rawDataList = rawData.split(' ')
            command = rawDataList[0]
            value = float(rawDataList[1])
            processedData = [command,value]
            print('processed data from raw data is {}'.format(processedData))
            CheckData(processedData)
            
def CheckData(processedData):
    if processedData[0] == 'T1':
        tempDisplay.config(text = processedData[1])
    elif processedData[0] == 'SR':
        serialStatus.config(text='Connected')
    elif processedData[0] == 'H1':
        humidityDisplay.config(text = processedData[1])
    elif processedData[0] == 'D1':
        distanceDisplay.config(text = processedData[1])

def main():
    incomingSerialThread = threading.Thread(name='serialCheck',target=CheckIncomingSerial, daemon=True)
    incomingSerialThread.start()
    root.mainloop()
    
if __name__ == '__main__':
    main()