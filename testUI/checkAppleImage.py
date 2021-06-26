from cvs import *
import numpy as np
import os,sys

def checkAppleImage():
    strTmp = "hfs1.jpg"
    im1 = cvs.imread(strTmp)

    cvs.setLbs("长沙理工大学测控专业"+"苹果检测B116队"+"显示苹果原始图像")
    cvs.imshow(im1)
    sleep(1000)
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
        
        #类似灰度图像的掩膜
        tmp3=np.zeros(gray1.shape,np.uint8) #生成黑背景
        mask3=cv2.drawContours(tmp3,cnt,i,(255,255,255),-1)  #绘制轮廓，形成掩膜,-1轮廓内部被填充


        #图割
        bgdModel = np.zeros((1,65),np.float64)
        fgdModel = np.zeros((1,65),np.float64)
        mask3[mask3 == 255] = 1
        mask4, bgdModel, fgdModel = cv2.grabCut(im1,mask3,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)
        mask4[mask3 == 1] = 255
        cvs.setLbs("长沙理工大学测控专业苹果检测B116队,"+"显示提取的苹果图像,"+"1.苹果面积是"+str(area)+" 2.苹果周长是"+str(length))
        cvs.imshow(mask4)
        
        
        
def analyzeAppleImage(im1):
    
    gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    hsv1 = cv2.cvtColor(im1, cv2.COLOR_BGR2HSV)
    # define range of red color in HSV
    lower_red = np.array([0,50,50])
    upper_red = np.array([20,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv1,lower_red, upper_red)

    im2,cnt, hierarchy= cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #寻找轮廓 
    appleInfo = "没有检测到苹果(红色区域)"
    mask4 =  mask
    
    n=len(cnt)       #轮廓个数
    contoursImg=[]
    for i in range(n):
        length = cv2.arcLength(cnt[i], True)  #获取轮廓长度
        area = cv2.contourArea(cnt[i])        #
        if length <500 and area<500*500*0.1:
            continue
        
        #类似灰度图像的掩膜
        tmp3=np.zeros(gray1.shape,np.uint8) #生成黑背景
        mask3=cv2.drawContours(tmp3,cnt,i,(255,255,255),-1)  #绘制轮廓，形成掩膜,-1轮廓内部被填充


        #图割
        bgdModel = np.zeros((1,65),np.float64)
        fgdModel = np.zeros((1,65),np.float64)
        mask3[mask3 == 255] = 1
        mask4, bgdModel, fgdModel = cv2.grabCut(im1,mask3,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)
        mask4[mask3 == 1] = 255
        appleInfo ="苹果面积是"+str(area)+"苹果周长是"+str(length)
        return im2,mask,mask4,appleInfo
    
    return im2,mask,mask4,appleInfo
    