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
        
        
def buttonUpdates(status,buttons):
    """Activates or deactivates buttons based on the status of the game"""
    if status == 'gameover':
        buttons[0].deactivate()
        buttons[1].deactivate()
        buttons[2].activate()
        buttons[3].activate()
    elif status == 'stillplaying':
        buttons[0].deactivate()
        buttons[1].activate()
        buttons[2].deactivate()
        buttons[3].deactivate()
    elif status == 'newgame':
        buttons[0].activate()
        buttons[1].activate()
        buttons[2].deactivate()
        buttons[3].deactivate()

