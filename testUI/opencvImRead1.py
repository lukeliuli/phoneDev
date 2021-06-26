
# -*- coding: utf-8 -*-


from remi.gui import *
from widgets.toolbox_opencv import *
from cvs import *

stopFlag = False
class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        self.opencvimread.update()
        self.opencvvideowidget.update()
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
        
        opencvimread0 = OpencvImRead()
        opencvimread0.attr_editor_newclass = False
        opencvimread0.css_height = "180px"
        opencvimread0.css_margin = "0px"
        opencvimread0.css_order = "547346434256"
        opencvimread0.css_position = "static"
        opencvimread0.css_top = "10px"
        opencvimread0.css_width = "200px"
        opencvimread0.filename = "anxi.jpg"
        opencvimread0.variable_name = "opencvimread0"
        container0.append(opencvimread0,'opencvimread0')
        
        opencvvideowidget1 = OpencvVideoWidget(self)
        opencvvideowidget1.attr_editor_newclass = False
        opencvvideowidget1.css_height = "180px"
        opencvvideowidget1.css_margin = "0px"
        opencvvideowidget1.css_order = "-1"
        opencvvideowidget1.css_position = "absolute"
        opencvvideowidget1.css_top = "220px"
        opencvvideowidget1.css_left = "20px"#调节没有用
        opencvvideowidget1.css_width = "200px"
        opencvvideowidget1.framerate = 10
        opencvvideowidget1.variable_name = "opencvvideowidget1"
        opencvvideowidget1.identifier="myimage_receiver"# = 0
        container0.append(opencvvideowidget1,'opencvvideowidget1')
        
        
        
        self.container0 = container0
        self.opencvimread = opencvimread0
        self.opencvvideowidget= opencvvideowidget1
        return self.container0
    
  



#processing_code

def process():
    
    counter = 0
    strTmp = "hfs1.jpg"
    print("readImage")
    im1 = cvs.imread(strTmp)
    while stopFlag is False:
        counter = counter+1
        sleep(100)
        cvs.imshow(im1)
        
  
    

if __name__ == "__main__":
    initcv(process)
    startcv(untitled)

