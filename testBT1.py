import android, time, sys,os
import json


#get everything setup
droid = android.Android()

locAddr = droid.bluetoothGetLocalAddress()
locName = droid.bluetoothGetLocalName()
print(locAddr)
print(locName)

rAddr = '38:E6:0A:3F:4F:22'#redmi5
#rAddr = '50:98:39:a9:5a:19'#redmi9
#rAddr = '88:BF:E4:C1:14:FC'#HUAWEI
#rName = droid.bluetoothGetRemoteDeviceName(rAddr)

#scanMode = droid.bluetoothGetScanMode()
#turn on bluetooth
droid.toggleBluetoothState(True)


counter = 0
#uuid = '00001101-0000-1000-8000-00805F9B34FB'
uuid = '457807c0-4897-11df-9879-0800200c9a66'
connID = ''
while counter < 100:
   
  time.sleep(1) 
  print("connecting")
  rvl = droid.bluetoothConnect(uuid,rAddr)
  print(rvl)
  #rvl = droid.bluetoothConnect('00001101-0000-1000-8000-00805F9B34FB')
  if rvl.error == None:
     connID = rvl.result
     connets = droid.bluetoothActiveConnections()
     print('connID='+connID)
     print(connets)
     break
        
  counter = counter+1
if counter>99:
    droid.exit()
    os.exit(0)
    
time.sleep(1) 
#https://wenku.baidu.com/view/59c2b2849e31433238689323.html



#sstr = "liuli"
#droid.bluetoothWrite(sstr + '\n') #otherwise write the message

while True: #receives a message
  time.sleep(1)
  print('send and waiting')
  droid.bluetoothWrite('Redmi9 send to Server' + '\n',connID) #otherwise write the message
  message = droid.bluetoothReadLine(connID).result
  print('Rcv Msg :'+message)  

droid.exit()
