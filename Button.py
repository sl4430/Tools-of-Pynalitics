import sys
from graphics import *

class Button:
    def __init__(self, start, center, width, height, size,text,s):
        x = center.getX()
        y = center.getY()
        self.x_max = x+width / 2.0
        self.x_min = x-width / 2.0
        self.y_max = y+height / 2.0
        self.y_min = y-height / 2.0
        p1 = Point(self.x_min, self.y_min)
        p2 = Point(self.x_max, self.y_max)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('green')
        self.rect.draw(start)
        self.text = Text(center, text)
        self.text.setSize(size)
        self.text.draw(start)
        if s is True:
            self.activate()
        else:
            self.deactivate()
            
    
    def activate(self): 
        #self.text.setFill('black')
        self.rect.setWidth(1)
        self.active = True
 
    def deactivate(self):
        #self.text.setFill('darkgreen')
        self.rect.setWidth(1)
        self.active = False

