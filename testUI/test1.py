
# -*- coding: utf-8 -*-


from remi.gui import *
from cvs import *
from checkAppleImage import *
from checkBTServer import *
from random import randint
stopFlag = False
global runFlag
runFlag = 1
global gInfo
gInfo = "空"

class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        self.aidcam.update()
        global gInfo
        self.info.text = gInfo
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        container0 = Container()
        container0.attr_editor_newclass = False
        container0.css_height = "675.0px"
        container0.css_left = "20px"
        container0.css_margin = "0px"
        container0.css_position = "absolute"
        container0.css_top = "20px"
        container0.css_width = "465.0px"
        container0.variable_name = "container0"
        teamName = Label()
        teamName.attr_editor_newclass = False
        teamName.css_color = "rgb(255,0,0)"
        teamName.css_font_size = "25px"
        teamName.css_height = "30.0px"
        teamName.css_left = "20px"
        teamName.css_margin = "0px"
        teamName.css_position = "absolute"
        teamName.css_top = "20px"
        teamName.css_width = "300.0px"
        teamName.text = "长沙理工大学测控专业B116苹果糖度检测"
        teamName.variable_name = "teamName"
        container0.append(teamName,'teamName')
        checkOpencv1 = Button()
        checkOpencv1.attr_editor_newclass = False
        checkOpencv1.css_height = "75px"
        checkOpencv1.css_left = "20px"
        checkOpencv1.css_margin = "0px"
        checkOpencv1.css_position = "absolute"
        checkOpencv1.css_top = "440px"
        checkOpencv1.css_width = "75px"
        checkOpencv1.text = "检测Opencv读取图像"
        checkOpencv1.variable_name = "checkOpencv1"
        container0.append(checkOpencv1,'checkOpencv1')
        checkOpencv2 = Button()
        checkOpencv2.attr_editor_newclass = False
        checkOpencv2.css_height = "75px"
        checkOpencv2.css_left = "110px"
        checkOpencv2.css_margin = "0px"
        checkOpencv2.css_position = "absolute"
        checkOpencv2.css_top = "440px"
        checkOpencv2.css_width = "75px"
        checkOpencv2.text = "检测Opencv摄像头"
        checkOpencv2.variable_name = "checkOpencv2"
        container0.append(checkOpencv2,'checkOpencv2')
        checkBluetooth = Button()
        checkBluetooth.attr_editor_newclass = False
        checkBluetooth.css_height = "75px"
        checkBluetooth.css_left = "200px"
        checkBluetooth.css_margin = "0px"
        checkBluetooth.css_position = "absolute"
        checkBluetooth.css_top = "440px"
        checkBluetooth.css_width = "75px"
        checkBluetooth.text = "检测蓝牙串口"
        checkBluetooth.variable_name = "checkBluetooth"
        container0.append(checkBluetooth,'checkBluetooth')
        
        checkUSBOTG = Button()
        checkUSBOTG.attr_editor_newclass = False
        checkUSBOTG.css_height = "75px"
        checkUSBOTG.css_left = "290px"
        checkUSBOTG.css_margin = "0px"
        checkUSBOTG.css_position = "absolute"
        checkUSBOTG.css_top = "440px"
        checkUSBOTG.css_width = "75px"
        checkUSBOTG.text = "检测USB串口"
        checkUSBOTG.variable_name = "checkUSBOTG"
        container0.append(checkUSBOTG,'checkUSBOTG')
        
        ###########################################################
        runOpencvBlue = Button()
        runOpencvBlue.attr_editor_newclass = False
        runOpencvBlue.css_height = "100px"
        runOpencvBlue.css_left = str(20)+"px"
        runOpencvBlue.css_margin = "0px"
        runOpencvBlue.css_position = "absolute"
        runOpencvBlue.css_top = "545px"
        runOpencvBlue.css_width = "100px"
        runOpencvBlue.text = "运行苹果糖度检测(opencv+蓝牙)"
        runOpencvBlue.variable_name = "runOpencvBlue"
        container0.append(runOpencvBlue,'runOpencvBlue')
        
        runOpencvUSB = Button()
        runOpencvUSB.attr_editor_newclass = False
        runOpencvUSB.css_height = "100px"
        runOpencvUSB.css_left = str(20+100+20)+"px"
        runOpencvUSB.css_margin = "0px"
        runOpencvUSB.css_position = "absolute"
        runOpencvUSB.css_top = "545px"
        runOpencvUSB.css_width = "100px"
        runOpencvUSB.text = "运行苹果糖度检测(opencv+USB)"
        runOpencvUSB.variable_name = "runOpencvUSB"
        container0.append(runOpencvUSB,'runOpencvUSB')
        
        info = Label()
        info.attr_editor_newclass = False
        info.css_height = "30px"
        info.css_left = "20px"
        info.css_margin = "0px"
        info.css_position = "absolute"
        info.css_top = "365px"
        info.css_width = "350px"
        info.text = "信息"
        info.variable_name = "info"
        container0.append(info,'info')
        
        cancel = Button()
        cancel.attr_editor_newclass = False
        cancel.css_height = "100px"
        cancel.css_left = str(20+100+20+100+20)+"px"
        cancel.css_margin = "0px"
        cancel.css_position = "absolute"
        cancel.css_top = "545px"
        cancel.css_width = "100px"
        cancel.text = "退出"
        cancel.variable_name = "cancel"
        container0.append(cancel,'cancel')
        
        opencvvideowidget1 = OpencvVideoWidget(self)
        opencvvideowidget1.attr_editor_newclass = False
        opencvvideowidget1.css_height = "180px"
        opencvvideowidget1.css_margin = "0px"
        opencvvideowidget1.css_order = "-1"
        opencvvideowidget1.css_position = "absolute"
        opencvvideowidget1.css_top = "120px"
        opencvvideowidget1.css_left = "20px"#调节没有用
        opencvvideowidget1.css_width = "200px"
        opencvvideowidget1.framerate = 30
        opencvvideowidget1.variable_name = "opencvvideowidget1"
        opencvvideowidget1.identifier="myimage_receiver"# = 0
        container0.append(opencvvideowidget1,'opencvvideowidget1')
        container0.children['checkOpencv1'].onclick.do(self.onclick_checkOpencv1)
        container0.children['checkOpencv2'].onclick.do(self.onclick_checkOpencv2)
        container0.children['checkBluetooth'].onclick.do(self.onclick_checkBluetooth)
        container0.children['checkUSBOTG'].onclick.do(self.onclick_checkUSBOTG)
        container0.children['runOpencvBlue'].onclick.do(self.onclick_runOpencvBlue)
        container0.children['cancel'].onclick.do(self.onclick_cancel)
        self.container0 = container0
        self.aidcam=opencvvideowidget1
        self.info =info
        return self.container0
    
    def onclick_checkOpencv1(self, emitter):
        self.info.text = "检查Opencv固定图像读取10次"
        print("检查Opencv固定图像读取10次")
        global gInfo
        gInfo = "检查Opencv固定图像读取10次"
        
        global runFlag
        runFlag = 2
        pass

    def onclick_checkOpencv2(self, emitter):
        self.info.text = "检查Opencv视频10秒"
        print("检查Opencv视频10秒")
        global gInfo
        gInfo = "检查Opencv视频10秒"
        global runFlag
        runFlag = 1
        pass

    def onclick_checkBluetooth(self, emitter):
        self.info.text = "检测蓝牙串口"
        global gInfo
        gInfo = "检测蓝牙串口"
        
        checkBTServer()
        pass

    def onclick_checkUSBOTG(self, emitter):
        self.info.text = "检测USBOTG串口"
        global gInfo
        gInfo = "检测USBOTG串口"
        pass

    def onclick_runOpencvBlue(self, emitter):
        self.info.text = "运行苹果糖度检测1"
        global gInfo
        gInfo = "运行苹果糖度检测1"
        global runFlag
        runFlag = 3
        
        pass

    def onclick_cancel(self, emitter):
        self.info.text = "直接点窗体上的退出按钮，有利于系统释放资源"
        global gInfo
        gInfo = "直接点窗体上的退出按钮，有利于系统释放资源"
        print("3秒后退出")
        global runFlag
        runFlag = 101
        
        pass




#processing_code

def process():
    
    img2 = cvs.imread("./res/anxi.jpg")
    global runFlag
    cap=cvs.VideoCapture(0)
    counter = 0
    while stopFlag is False:
        if runFlag == 1:
            sleep(33)
            img =cap.read()
            if img is None :
                continue
            cvs.imshow(img)
            
            counter = counter+1
            counter = counter%30*10
            if counter==0:
                  runFlag = 1
                  print("视频检测10秒到了")
        
        elif runFlag == 2:
           
            checkAppleImage()
            sleep(1000)
            
            counter = counter+1
            counter = counter%11
            if counter==0:
                  runFlag = 1
                  print("苹果检测10次到了")
        
        elif runFlag == 3:
            img =cap.read()
            if img is None :
                continue
            cvs.imshow(img)
            tmp = randint(1,10000)
            
            strTmp = str(tmp)+"capture"+".jpg"
            cv2.imwrite(strTmp,img)
            
            imContour,redMask,appleMask,appleInfo=analyzeAppleImage(img)
            
            strTmp = str(tmp)+"imContour"+".jpg"
            cv2.imwrite(strTmp,imContour)
            
            strTmp = str(tmp)+"redMask"+".jpg"
            cv2.imwrite(strTmp,redMask)
            
            strTmp = str(tmp)+"appleMask"+".jpg"
            cv2.imwrite(strTmp,appleMask)
            print(appleInfo)
            global gInfo
            gInfo = appleInfo
            sleep(1000)
            
            counter = counter+1
            counter = counter%5
            if counter==0:
                  runFlag = 1
                  print("检测5次，每次1秒")
            
            
        else:
            
            cvs.imshow(img2)
            sleep(1000)
        
        
       
       
    
if __name__ == "__main__":
    initcv(process)
    startcv(untitled)

