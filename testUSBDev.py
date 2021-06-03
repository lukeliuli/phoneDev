import android, time, sys
import json

droid = android.Android()

#import caffe

# droid.webViewShow('http://127.0.0.1:8000')

droid.makeToast("测试USB串口")
time.sleep(1)


h = None
n = 0

for k, v in droid.usbserialGetDeviceList().result.items():
    print("device lists:",k, v)

    time.sleep(1)
    
    
    if '"1A86","7523"' in v:
            h = json.loads(v)[-1]
            print("device was found, try to connect =>", h)
            
    ret = droid.usbserialConnect(h, ",7523,")
    # ret = droid.usbserialConnect(h, ",pl2303,")
    print ("connect...",ret)
    if not "OK" in ret.result:
        print("can't connect to device: ", ret.result)
        # return
        
    
    
    uuid = json.loads(ret.result)[-1]
    print("OK OK OK connected with ", h, uuid)
    
    # send='hello,world'
    # droid.usbserialWrite(send, uuid)
    # wait until the permission be allowed by user.
    '''    
    while not droid.usbserialReadReady(uuid).result:
         n += 1
         print("waiting for connect....", n)
         time.sleep(1)
    '''
    
    
    # now get data from USB-Serial.
 
    while True:
        time.sleep(0.1)

        buf= droid.usbserialRead(uuid)
        print("Received: ", buf)
        print("Received: ", buf.result)
        send = 'rev OK'
        #buf = droid.usbserialWrite(send, uuid)
