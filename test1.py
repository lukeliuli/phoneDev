#集成一切，进行学习"""
#api 例子 https://blog.csdn.net/jiguanghoverli/article/details/7278109
#api例子 https://pingu98.wordpress.com/tag/sl4a/
#https://www.qpython.org/en/guide_androidhelpers.html#webcamfacade
#http://www.vue5.com/sl4a/sl4a_quick_guide.html
__author__ = 'liuli <lukeliuli@163.com>'
__copyright__ = 'Copyright (c) 2021, csust.'
__license__ = 'Apache License, Version 2.0'

import androidhelper
import time
import qpy
import sys
import time
droid = androidhelper.Android()

##
msg = "欢迎光临"

droid.makeToast(msg)
#droid.notify('Test Title', 'Hello, world!')
#droid.dialogCreateAlert("Hello", "QPython")
#读写文本
"""
droid.ttsSpeak(time.strftime("刘老师，现在时间为%Y年%m月%d日%H小时%M分%S秒"))
droid.ttsSpeak("请输入你要读的文字")
message = droid.dialogGetInput('TTS', '请输入你要读的文字:').result
droid.ttsSpeak(message)
"""

#拍摄图像
"""
strTmp = qpy.tmp+"/test.png"
strTmp = "/storage/emulated/0/test.png"
#ret = droid.cameraCapturePicture(strTmp).result
ret = droid. cameraInteractiveCapturePicture(strTmp).result

print("Result:"+str(ret))
print("Please open "+strTmp+" to check the picutre")
"""
##振动1秒
droid.vibrate(1000)

##发送短信
droid.smsSend("18874072838","QPython测试")

##获得网络状态
ret = droid.getNetworkStatus()
print(ret)


#传感器看http://www.mithril.com.au/android/doc/SensorManagerFacade.html
#https://blog.csdn.net/weixin_33856370/article/details/92129020
droid.startSensingTimed(1, 250)
time.sleep(1)
s1 = droid.readSensors().result
s2 = droid.sensorsGetAccuracy().result
s3 = droid.sensorsGetLight().result
s4 = droid.sensorsReadAccelerometer().result
s5 = droid.sensorsReadMagnetometer().result
s6 = droid.sensorsReadOrientation().result
droid.stopSensing()
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

##GPS定位
droid.startLocating()
time.sleep(1)
loc = droid.readLocation().result
if loc == {}:
 loc = getLastKnownLocation().result
if loc != {}:
 try:
   n = loc['gps']
 except KeyError:
   n = loc['network'] 
 la = n['latitude'] 
 lo = n['longitude']
 address = droid.geocode(la, lo).result
 print(address)
 print(la)
 print(lo)
droid.stopLocating()


#wifi信号强度
ret = droid.wifiGetConnectionInfo()
print(ret)


#网络信号强度
ret = droid.readSignalStrengths().result
print(ret)
 
##获得摄像头，并且把图像存到文件中，注意这个方式已经放弃，因为实时存储文件，文件大
"""
picdir = qpy.tmp
#droid.webcamAdjustQuality(3, 20)
droid.cameraStartPreview(100,80,picdir)
time.sleep(1)
droid.cameraStopPreview()
"""
##获得摄像头，并且把图像变为一个MJPEG服务器
#address = droid.webcamStart(100,80,0).result
#time.sleep(1)
#print(address)

#电池
"""
droid.batteryStartMonitoring()
time.sleep(5)
bdata = droid.readBatteryData()
print(bdata.result)

bstatus = droid.batteryGetStatus().result
bhealth = droid.batteryGetHealth().result
bplug = droid.batteryGetPlugType().result
bcheck = droid.batteryCheckPresent().result
blevel = droid.batteryGetLevel().result
bvoltage = droid.batteryGetVoltage().result
btemperature = droid.batteryGetTemperature().result
btechnology = droid.batteryGetTechnology().result
print("电池",{"status": bstatus, "health": bhealth, "plugtype": bplug, "checkpresent": bcheck, "level": blevel, "voltage": bvoltage, "temperature": btemperature, "technology": btechnology})

droid.batteryStopMonitoring()
"""

#SL4A与蓝牙GPS
#https://blog.csdn.net/weixin_39967938/article/details/111786821
#其余的功能，如播放音视频，NFC, 录制音视频，与项目无关，暂时不实现

#USB串口
#https://github.com/giuliolunati/sl4abox/blob/17658561f2aa1b7ec9ee2b4051524a1c7d80c1cd/android/USBHostSerialFacade/samplescripts/testpl2303.py
ret = droid.usbserialGetDeviceList().result
print(ret)

for k, v in droid.usbserialGetDeviceList().result.items():
    print(k, v)

