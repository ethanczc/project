from tkinter import*
import time
import threading
import serial

root= Tk()
root.title('serial test')
root.geometry('400x200')

#ser = serial.Serial('/dev/ttyUSB0',9600)

def SerialConnect():
    ser = serial.Serial('/dev/ttyUSB0',9600)
    print('connection to USB0 successful')
    
def SendSerial():
    message = serialEntry.get()
    ser.write(message.encode()) #encode message before sending to arduino

serialAddressLabel = Label(root, text='Serial Address').grid(row=1,column=0)
serialAddressEntry = Entry(root)
serialAddressEntry.grid(row=1,column=1)

serialConnectButton = Button(root, text='Serial Connect',command=SerialConnect)
serialConnectButton.grid(row=2,column=0,columnspan=2)

serialStatusLabel = Label(root, text='Serial Status').grid(row=3,column=0)
serialStatus = Label(root, text = 'Disconnected')
serialStatus.grid(row=3, column=1)

serialEntryLabel = Label(root, text='Serial Command').grid(row=4,column=0)
serialEntry = Entry(root)
serialEntry.grid(row=4, column=1)

serialSendButton = Button(root, text='send serial', command = SendSerial)
serialSendButton.grid(row=5,column=0,columnspan=2)

def CheckIncomingSerial():
    while True:
        try:
            rawData = ser.readline()
        except:
            pass
        else:
            rawData = rawData.decode('utf-8') #decode message from arduino
            rawData = rawData[:-2] #splice off \r\n
            print('raw data received is {}'.format(rawData))
            if rawData == 'Connected':
                serialStatus.config(text='connected')
            
def main():
    incomingSerialThread = threading.Thread(name='serialCheck',target=CheckIncomingSerial, daemon=True)
    incomingSerialThread.start()
    root.mainloop()
    
if __name__ == '__main__':
    main()