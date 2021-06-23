
#只做OPENCV
__author__ = 'liuli <lukeliuli@163.com>'
__copyright__ = 'Copyright (c) 2021, csust.'
__license__ = 'Apache License, Version 2.0'

# androidhelper qpython 用这个
#droid = androidhelper.Android()
import android #aidlearning和sla4用这个
import time
from cvs import *
import numpy as np


droid=android.Android()
##
msg = "测试open C V"
droid.makeToast(msg)
droid.ttsSpeak(msg)
time.sleep(5)


#https://docs.opencv.org/4.5.2/df/d9d/tutorial_py_colorspaces.html
#读取苹果图像，显示苹果大小，红色
strTmp = "hfs1.jpg"
im1 = cvs.imread(strTmp)
cvs.imshow(im1)
droid.ttsSpeak("读取图像OK和显示苹果原始图像")
time.sleep(5)

gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
hsv1 = cv2.cvtColor(im1, cv2.COLOR_BGR2HSV)
# define range of red color in HSV
lower_red = np.array([0,50,50])
upper_red = np.array([20,255,255])
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv1,lower_red, upper_red)

im2,cnt, hierarchy= cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #寻找轮廓 

n=len(cnt)       #轮廓个数
contoursImg=[]
for i in range(n):
    length = cv2.arcLength(cnt[i], True)  #获取轮廓长度
    area = cv2.contourArea(cnt[i])        #
    if length <500 and area<500*500*0.1:
        continue
    print('length['+str(i)+']长度=',length)
    print("contours["+str(i)+"]面积=",area)
 
    
    #类似灰度图像的掩膜
    tmp3=np.zeros(gray1.shape,np.uint8) #生成黑背景
    mask3=cv2.drawContours(tmp3,cnt,i,(255,255,255),-1)  #绘制轮廓，形成掩膜,-1轮廓内部被填充

    
    #图割
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    mask3[mask3 == 255] = 1
    mask4, bgdModel, fgdModel = cv2.grabCut(im1,mask3,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)
    mask4[mask3 == 1] = 255
    cvs.imshow(mask4,"test opencv grabCut")
    
    droid.ttsSpeak("显示提取的苹果图像")
    droid.ttsSpeak("苹果面积是"+str(area))
    droid.ttsSpeak("苹果周长是"+str(length))
  
  
    
    
time.sleep(5)
exit(0)

import apkneed

