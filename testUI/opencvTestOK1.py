
# -*- coding: utf-8 -*-


from remi.gui import *
from widgets.toolbox_opencv import *
from cvs import *


class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        self.aidcam.update()
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        vbox0 = VBox()
        vbox0.attr_editor_newclass = False
        vbox0.css_align_items = "center"
        vbox0.css_display = "flex"
        vbox0.css_flex_direction = "column"
        vbox0.css_height = "250px"
        vbox0.css_justify_content = "space-around"
        vbox0.css_left = "20px"
        vbox0.css_margin = "0px"
        vbox0.css_position = "absolute"
        vbox0.css_top = "20px"
        vbox0.css_width = "250px"
        vbox0.variable_name = "vbox0"
        vbox1 = VBox()
        vbox1.attr_editor_newclass = False
        vbox1.css_align_items = "center"
        vbox1.css_display = "flex"
        vbox1.css_flex_direction = "column"
        vbox1.css_height = "250px"
        vbox1.css_justify_content = "space-around"
        vbox1.css_margin = "0px"
        vbox1.css_order = "511041162880"
        vbox1.css_position = "static"
        vbox1.css_top = "20px"
        vbox1.css_width = "250px"
        vbox1.variable_name = "vbox1"
        opencvvideowidget1 = OpencvVideoWidget(self)
        opencvvideowidget1.attr_editor_newclass = False
        opencvvideowidget1.css_height = "180px"
        opencvvideowidget1.css_margin = "0px"
        opencvvideowidget1.css_order = "-1"
        opencvvideowidget1.css_position = "static"
        opencvvideowidget1.css_top = "10px"
        opencvvideowidget1.css_width = "200px"
        opencvvideowidget1.framerate = 10
        opencvvideowidget1.variable_name = "opencvvideowidget1"
        opencvvideowidget1.identifier="myimage_receiver"# = 0
        vbox1.append(opencvvideowidget1,'opencvvideowidget1')
        vbox0.append(vbox1,'vbox1')
        

        self.vbox0 = vbox0
        self.aidcam=opencvvideowidget1
        return self.vbox0
    



#processing_code

def process():

    cap=cvs.VideoCapture(1)
    
    while True:
        sleep(30)
        img =cap.read()

        if img is None :
            continue
        cvs.imshow(img)

if __name__ == "__main__":
    initcv(process)
    startcv(untitled)

