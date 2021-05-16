
#只做OPENCV
__author__ = 'liuli <lukeliuli@163.com>'
__copyright__ = 'Copyright (c) 2021, csust.'
__license__ = 'Apache License, Version 2.0'

# androidhelper qpython 用这个
#droid = androidhelper.Android()
import android #aidlearning和sla4用这个
import json
import sys
import time
from cvs import *
import cv2
import cv2 as cv
droid=android.Android()
##
msg = "测试opencv"
droid.makeToast(msg)

#从摄像头获取图像1.基于sl4a
"""
strTmp = "/home/camCap.png"#只能是png图像
ret = droid.cameraCapturePicture(strTmp).result
#ret = droid.cameraInteractiveCapturePicture(strTmp).result
print("Result:"+str(ret))
print("Please open "+strTmp+" to check the picutre")
"""
#从摄像头获取图像2,基于OPENCV
"""
from cvs import *
import numpy as np
cap=cvs.VideoCapture(1)#打开摄像头1
time.sleep(1)
img =cap.read()#读取一帧图像
cvs.imshow(img)#显示图片
"""
#https://docs.opencv.org/4.5.2/df/d9d/tutorial_py_colorspaces.html
#读取苹果图像，显示苹果大小，红色
strTmp = "/home/githubcodes/phoneDev/hfs1.jpg"
im1 = cvs.imread(strTmp)
#cvs.imshow(im1)

gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
hsv1 = cv2.cvtColor(im1, cv2.COLOR_BGR2HSV)
# define range of red color in HSV
lower_red = np.array([0,50,50])
upper_red = np.array([20,255,255])
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv1,lower_red, upper_red)
# Bitwise-AND mask and original image
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15))
#opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#closing = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

#轮廓https://blog.csdn.net/hjxu2016/article/details/77833336/
#cvs.imshow(mask)
im2,cnt, hierarchy= cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #寻找轮廓 
cv2.drawContours(im1,cnt,-1,(0,255,0),3)  

cvs.imshow(im1,"1")
#print(len(cnt))  

area = cv2.contourArea(cnt)
print(area)

"""
ellipse = cv.fitEllipse(cnt)
cv.ellipse(im1,ellipse,(0,255,0),2)
cvs.imshow(im1,"1")

epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)
hull = cv.convexHull(cnt)

#mask = opening(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img,center,radius,(0,255,0),2)

ellipse = cv.fitEllipse(cnt)
cv.ellipse(img,ellipse,(0,255,0),2)

res = cv2.bitwise_and(im1,im1, mask=mask)
cvs.imshow(mask)
time.sleep(5)
cvs.imshow(res)
time.sleep(5)
exit(0)
"""