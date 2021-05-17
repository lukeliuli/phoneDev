
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

import numpy as np
from matplotlib import pyplot as plt

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

#轮廓
# https://blog.csdn.net/hjxu2016/article/details/77833336/
#https://blog.csdn.net/weixin_40922285/article/details/102843938
#cvs.imshow(mask)
im2,cnt, hierarchy= cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #寻找轮廓 
print(len(cnt))  
#cv2.drawContours(im1,cnt,-1,(0,255,0),3)  
#cvs.imshow(mask,"1")

n=len(cnt)       #轮廓个数
contoursImg=[]
for i in range(n):
    length = cv2.arcLength(cnt[i], True)  #获取轮廓长度
    area = cv2.contourArea(cnt[i])        #
    if length <500 and area<500*500*0.1:
        continue
    print('length['+str(i)+']长度=',length)
    print("contours["+str(i)+"]面积=",area)
    tmp1=np.zeros(im1.shape,np.uint8) #生成黑背景
   
    tmp2=cv2.drawContours(tmp1,cnt,i,(255,255,255), 3)  #绘制轮廓
    #cvs.imshow(tmp2)   #显示轮廓

    mask=cv2.drawContours(tmp1,cnt,i,(255,255,255),-1)  #绘制轮廓，形成掩膜,-1轮廓内部被填充
    #cvs.imshow(mask)        #显
    
    #类似灰度图像的掩膜
    tmp3=np.zeros(gray1.shape,np.uint8) #生成黑背景
    mask3=cv2.drawContours(tmp3,cnt,i,(255,255,255),-1)  #绘制轮廓，形成掩膜,-1轮廓内部被填充
    cvs.imshow(mask3)
    
    result=cv2.bitwise_and(im1,mask)   #按位与操作，得到掩膜区域
    #cvs.imshow(result)     #显示图像中提取掩膜区域
    

    #多变型外接凸轮廓
    #epsilon = 0.1*cv.arcLength(cnt[i],True)
    #approx = cv.approxPolyDP(cnt[i],epsilon,True)
    #hull = cv.convexHull(cnt[i])
    #ret = cv2.drawContours(im1,[hull],0,(255,0,0),3)
    #cvs.imshow(ret)
    
    #外接椭圆
    #ellipse = cv.fitEllipse(cnt[i])
    #cv.ellipse(im1,ellipse,(0,255,0),2)
    #cvs.imshow(im1,"1")
    
    ##最小外接园
    #(x,y),radius  = cv.minEnclosingCircle(cnt[i])
    #center = (int(x),int(y))
    #radius = int(radius)
    #cv.circle(im1,center,radius,(0,255,0),2)
    #cvs.imshow(im1,"1")

    """
    #方框和最小面积方框
    x,y,w,h = cv2.boundingRect(cnt[i])  #轮廓点
    result1 = cv2.rectangle(im1,(x,y),(x+w,y+h),(0,255,0),2)  #构造矩形方框
    rect = cv2.minAreaRect(cnt[i])  #最小面积方框
    points = cv2.boxPoints(rect)
    points = np.int0(points)  #取整
    result2=cv2.drawContours(im1,[points],0,(255,0,0),2)
    cvs.imshow(im1,"1")
    """

    """
    ##寻找三角形
    area,trgl = cv2.minEnclosingTriangle(contours[0])  #寻找三角形
    for i in range(0, 3):                               #绘制三角形
        result5 = cv2.line(im1, tuple(trgl[i][0]), tuple(trgl[(i + 1) % 3][0]), (255,255,255), 2)
    """
    #直方图
    #https://www.jianshu.com/p/
    """
    print(mask3.shape)
    print(mask3.dtype)
    #mask3 = (mask3 > 230).astype(np.uint8)
    
    
    hist=cv2.calcHist([hsv1],[0], mask3, [10], [0,180])
    print(hist.shape)
    for i in range(len(hist)):
        print('%8d' %hist[i])
    #plt.figure()
    #plt.title("Grayscale Histogram")
    #plt.xlabel("Bins")
    #plt.ylabel("# of Pixels")
    #plt.plot(hist)
    """
    
    #图割
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    mask3[mask3 == 255] = 1
    mask4, bgdModel, fgdModel = cv.grabCut(im1,mask3,None,bgdModel,fgdModel,5,cv.GC_INIT_WITH_MASK)
    mask4[mask3 == 1] = 255
    #cvs.imshow(mask4,"1")
    

    #https://docs.opencv.org/3.4.14/dc/df6/tutorial_py_histogram_backprojection.html
    hist=cv2.calcHist([hsv1],[0], mask3, [180], [0,180])
    cv.normalize(hist,hist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([hsv1],[0],hist,[0,180],1)
    #disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
    #cv.filter2D(dst,-1,disc,dst)
    ret,thresh = cv.threshold(dst,50,255,0)
    disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, disc)
    disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(15,15))
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, disc)
    cvs.imshow(closing,"1")


    #多个苹果分割，采用距离变换+watershed
    #https://docs.opencv.org/3.4.14/d3/db4/tutorial_py_watershed.html
    
    
time.sleep(5)
exit(0)
