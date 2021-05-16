
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

droid=android.Android()
##
msg = "测试opencv"
droid.makeToast(msg)

#从摄像头获取图像
strTmp = "/home/camCap.png"#只能是png图像
ret = droid.cameraCapturePicture(strTmp).result
#ret = droid.cameraInteractiveCapturePicture(strTmp).result
print("Result:"+str(ret))
print("Please open "+strTmp+" to check the picutre")

#
strTmp = "/home/githubcodes/phaneDev/hfs1.jpg"