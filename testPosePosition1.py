#集成一切，进行学习"""
#api 例子 https://blog.csdn.net/jiguanghoverli/article/details/7278109
#api例子 https://pingu98.wordpress.com/tag/sl4a/
#https://www.qpython.org/en/guide_androidhelpers.html#webcamfacade
#http://www.vue5.com/sl4a/sl4a_quick_guide.html
__author__ = 'liuli <lukeliuli@163.com>'
__copyright__ = 'Copyright (c) 2021, csust.'
__license__ = 'Apache License, Version 2.0'

import sys
import time
# androidhelper qpython 用这个
#droid = androidhelper.Android()
import android #aidlearning和sla4用这个

import sys
import time
import datetime
import numpy as np
import math

droid = android.Android()
##振动1秒
droid.vibrate(1000)



#传感器
##http://www.mithril.com.au/android/doc/SensorManagerFacade.html
#https://blog.csdn.net/weixin_33856370/article/details/92129020

dt = 10
droid.startSensingTimed(1,  dt)
time.sleep(5)
s1 = droid.readSensors().result
counter = 0
#{'accuracy': 3, 'xforce': -0.0852522, 'yforce': -0.033089522, 'zforce': 9.840513, 'azimuth': -0.8604623436927795, 'roll': 0.007939949072897435, 'time': 1621413794.494, 'xMag': 13.692818, 'yMag': 11.835213, 'zMag': 39.815357, 'light': 175, 'pitch': 0.005386198777705431}
#x水平朝右为正
#y水平向前为正
#z垂直向上为正

xf = []
yf = []
zf = []
xt = []
roll = []
azimuth = []
pitch = []
rtime = []
initTime =0
while counter<50*10:
    
    s1 = droid.readSensors().result
    
    #print(s1)
    #s4 = droid.sensorsReadAccelerometer().result
    #s5 = droid.sensorsReadMagnetometer().result
    #s6 = droid.sensorsReadOrientation().result
   
    xf.append(s1["xforce"])
    yf.append(s1["yforce"])
    zf.append(s1["zforce"])
    roll.append(math.degrees(s1["roll"]))
    azimuth.append(math.degrees(s1["azimuth"]))
    pitch.append(math.degrees(s1["pitch"]))
    if counter == 0:
        initTime = s1["time"]
        #initTime = 0
    rtime.append(s1["time"] - initTime)

    #s=time.strftime("%Y-%m-%d %H:%M:%S.%f")
    s=datetime.datetime.now().strftime("%H:%M:%S.%f")
    counter=counter+1
    #print(s)
    #tmp = tmp +s1["xforce"]
    '''
    print("----------------------------")
    print(roll[-1])
    print(pitch[-1])
    print(azimuth[-1])
    '''


    time.sleep(0.01)
 
#xfAvg = np.mean(xf)
#xfStd = np.std(xf)
rollDiff = [ roll[i+1]-roll[i] for i in range(len(roll)-1)]
pitchDiff = [ pitch[i+1]-pitch[i] for i in range(len(pitch)-1)]
azimuthDiff = [ azimuth[i+1]-azimuth[i] for i in range(len(azimuth)-1)]
yfDiff = [ azimuth[i+1]-azimuth[i] for i in range(len(yf)-1)]

rollDiffAvg = np.mean(rollDiff )
rollDiffStd = np.std(rollDiff)

pitchDiffAvg = np.mean(pitchDiff)
pitchDiffStd = np.std(pitchDiff)

azimuthDiffAvg = np.mean(azimuthDiff)
azimuthDiffStd = np.std(azimuthDiff)

yfAvg =  np.mean(yf)
yfStd =  np.std(yf)
yfDiffAvg =  np.mean(yfDiff)
yfDiffStd =  np.std(yfDiff)

print("rollDiff %.3f,%.3f"%(rollDiffAvg,rollDiffStd))

print("pitchDiff %.3f,%.3f"   %(pitchDiffAvg,pitchDiffStd))

print("azimuthDiff %.3f,%.3f" %(azimuthDiffAvg,azimuthDiffStd))

print("yfDiff %.3f,%.3f" %(yfDiffAvg,yfDiffStd))
print("yf %.3f,%.3f" %(yfAvg,yfStd))

exit(0)
#scipy 积分 http://liao.cpython.org/scipy18/
#https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html
#https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.integrate.simps.html
from scipy import integrate
#print(rtime)
#xv1 = integrate.simps(xf,rtime)
#print(xv1)
#xfTmp = [a-xfAvg for a in xf] 
#xv2 = integrate.simps(xfTmp,rtime)
#print(xv2)
#xv3 = integrate.cumtrapz(xfTmp,rtime, initial=0)
#print(xv3)
#print(xv3[-1])
#v0Mean = np.mean(xv3)
#print(xv3.shape)
#print(len(xfTmp))

#xv4 = integrate.cumtrapz(xv3,rtime, initial=0)
#print(xv3)
#print(xv4[-1])
#print(xv3.shape)
#print(len(xfTmp))

##############################################################
xf = []
yf = []
zf = []
roll = []
azimuth = []
pitch = []
rtime = []
initTime =0
xv3 = []
xv4 = []
####https://blog.csdn.net/wh_19910525/article/details/13774479
#1. azimuth 方位角：就是绕z轴转动的角度，0度=正北,（假设Y轴指向地磁正北方，直升机正前方的方向如下图
#2. pitch 仰俯：绕X轴转动的角度 (-180<=pitch<=180), 如果设备水平放置，前方向下俯就是正，如图
#3. roll 滚转：绕Y轴转动(-90<=roll<=90)，向左翻滚是正值
counter = 0
vel0y = 0
dt = 0.01
print("start")
while counter<100000:
   
    s1 = droid.readSensors().result
    
    xf.append(s1["xforce"])
    yf.append(s1["yforce"])
    zf.append(s1["zforce"])
    roll.append(math.degrees(s1["roll"]))
    azimuth.append(math.degrees(s1["azimuth"]))
    pitch.append(math.degrees(s1["pitch"]))
    if counter == 0:
       initTime = s1["time"]
    #initTime = 0
    rtime.append(s1["time"] - initTime)


    counter=counter+1
    if counter%100==99 and len(yf)>100:
        #print(len(yf))
        #print(len(rtime))
        ##滤波
        conv_size = 100
        yf1 = np.convolve(yf,np.ones(conv_size),'same')/conv_size
        
        #print(yf1.shape)
        for ii in range(len(yf1)-1):
            veloY[ii]= velY0+ yf1[ii]*dt+ (yf1[ii+1]-yf1[ii])*dt/2
            velocityx[1]= vel0+ yf1[ii]*dt+ (yf1[ii+1]-yf1[ii])*dt/2

        yv3 = integrate.cumtrapz(yf1,rtime,initial=0)

        for i in range(len(yf1)-1):
           if abs(pitch[i]-pitch[i+1])<0.25:
                yv3[i]=0
                yf1[i]=0
                yv3[i+1]=0
                yf1[i+1]=0
        

        #yv4 = np.trapz(yv3)*0.01
        #yv4 = integrate.simps(yv3,rtime)
        yv4 = integrate.cumtrapz(yv3,rtime)
        print("------------------")
        print(yf1[-1])
        print(yv3[-1])
        print(yv4)
    
        #yv4 = np.trapz(yv3)*0.01
        #print(yv4)
        #yv4 = integrate.cumtrapz(yv3,rtime)
        #print(yv4[-1])

        #yv3 = integrate.simps(yf,rtime)
        #print(yv3)
        #yv4 = integrate.simps(yv3,dx=0.01)

        
        
      
     
    
    time.sleep(0.01)

droid.stopSensing()

