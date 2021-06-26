import androidhelper,sys
import time
from cvs import *

def checkBTServer()
    #担心蓝牙socket被上一个程序锁了
    droid = androidhelper.Android()
    droid.bluetoothStop()
    droid.toggleBluetoothState(False)
    sleep(100)
    droid.toggleBluetoothState(True)
    locAddr = droid.bluetoothGetLocalAddress()
    locName = droid.bluetoothGetLocalName()
    print(locAddr)
    print(locName)

    #uuid ='00001101-0000-1000-8000-00805F9B34FB'
    uuid = '457807c0-4897-11df-9879-0800200c9a66'#uuid需要正确，看BT uuid定义

    droid.bluetoothMakeDiscoverable()
    
    connID = ''
    #rAddr = '38:E6:0A:3F:4F:22'#redmi5
    #rAddr = '50:98:39:a9:5a:19'#redmi9
    #rAddr = '88:BF:E4:C1:14:FC'#HUAWEI

    counter = 0
    while counter <100:#等待100秒
        time.sleep(1)
        print("waiting accepting")
        rvl = droid.bluetoothAccept(uuid,0)  
        #print(rvl)

        if rvl.error == None:
            connID = rvl.result
            connets = droid.bluetoothActiveConnections()
            print('connID='+connID)
            print(connets.result)
            break
            
        counter=counter+1
        #print(counter)

    if counter>99:#无蓝牙接入
        print('exit')
        droid.exit()
        return None
    
    counter = 0
    while counter <1000:#运行100秒
        time.sleep(100)
        droid.bluetoothWrite('Server Redmi5 send to Client' + '\n',connID) #otherwise write the message
        print("sending and waiting")
        message = droid.bluetoothReadLine(connID).result
        print('Rcv Msg:'+message) 
        counter=counter+1
        
    droid.exit()
    return 0
