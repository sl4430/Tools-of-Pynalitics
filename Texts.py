# This file deals with text display function for main game
# Author: Qifu Yin, Shujun Liu, Shixin Li, Di Zhu
# Date: 12-02-2018
from graphics import *

class text_box(Text):
    #Creates a box to record how much money left
    def __init__(self, win, center,text,value):
        x = center.getX()
        y = center.getY()

        self.text = Text(Point(x-15,y), text)
        self.text.setSize(12)
        self.text.draw(win)

        self.value = self.text.clone()
        self.value.move(32,0)
        self.value.setText(value)
        self.value.draw(win)

    def updateText(self,new_value):
        #change of remain money
        if self.value.getText() == new_value:
            pass
        else:
            self.value.setText(new_value)
            # Visual feedback when the value changes for the user
            for i in range(2):
                time.sleep(0.1)

                if i % 2 == 0:
                    self.value.setStyle('bold')
                else:
                    self.value.setStyle('normal')

def popText(win,center,text,timing):
    #flash the text to show user the win information
    win_info = Text(center,text)
    win_info.setFace("arial")
    win_info.setFill("black")
    win_info.setSize(30)
    win_info.draw(win)
    time.sleep(timing)
    win_info.undraw()
    
