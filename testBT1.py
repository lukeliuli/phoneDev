import android, time, sys
import json


#get everything setup
droid = android.Android()

locAddr = droid.bluetoothGetLocalAddress()
locName = droid.bluetoothGetLocalName()
print(locAddr)
print(locName)

rAddr = '38:E6:0A:3F:4F:22'
rName = droid.bluetoothGetRemoteDeviceName(rAddr)
print(rName)

#scanMode = droid.bluetoothGetScanMode()
#turn on bluetooth
droid.toggleBluetoothState(True)

#ask user

'''
droid.dialogCreateAlert('Be a server?')
droid.dialogSetPositiveButtonText('Yes')
droid.dialogSetNegativeButtonText('No')
droid.dialogShow()

#get user response to question
result = droid.dialogGetResponse()

#if the result is 'Yes' ('positive') then is_server is set to True
is_server = result.result['which'] == 'positive'
'''
counter = 0
uuid = '00001101-0000-1000-8000-00805F9B34FB'
#uuid = '457807c0-4897-11df-9879-0800200c9a66'
connID = ''
while counter < 10:
   
  time.sleep(1) 
  print("connecting")
  rvl = droid.bluetoothConnect('00001101-0000-1000-8000-00805F9B34FB','38:E6:0A:3F:4F:22')
  print(rvl)
  #rvl = droid.bluetoothConnect('00001101-0000-1000-8000-00805F9B34FB')
  if rvl.error == None:
     connID = rvl.result
     connets = droid.bluetoothActiveConnections()
     print(connets)
     name = droid.bluetoothGetConnectedDeviceName(connID)
     print(name)
     break
        
  counter = counter+1
 
time.sleep(10) 
#https://wenku.baidu.com/view/59c2b2849e31433238689323.html



#sstr = "liuli"
#droid.bluetoothWrite(sstr + '\n') #otherwise write the message

while True: #receives a message
  time.sleep(1)
  droid.bluetoothWrite('sending' + '\n',connID) #otherwise write the message
  print("waiting")
  #message = droid.bluetoothReadLine(connID).result
  #print(message)  

droid.exit()
