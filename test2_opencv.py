
#只做OPENCV
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


#拍摄图像

strTmp = qpy.tmp+"/test.png"
strTmp = "/storage/emulated/0/testApple1.png"
#ret = droid.cameraCapturePicture(strTmp).result
ret = droid. cameraInteractiveCapturePicture(strTmp).result
print("Result:"+str(ret))
print("Please open "+strTmp+" to check the picutre")


