
#只做OPENCV
__author__ = 'liuli <lukeliuli@163.com>'
__copyright__ = 'Copyright (c) 2021, csust.'
__license__ = 'Apache License, Version 2.0'

 androidhelper qpython 用这个
#droid = androidhelper.Android()
import android #aidlearning和sla4用这个
import json
import sys
import time
from cvs import *
#import cv2 as cv

import numpy as np

droid=android.Android()
##
msg = "测试opencv和kivy"
droid.makeToast(msg)