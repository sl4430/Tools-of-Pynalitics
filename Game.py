# The program that executes the game.
# Author: Qifu Yin
# Date: 12-27-2018

from graphics import *
import time
import random
import time
#from Deck import*
#from Button import*
#from Texts import*

class Game():
    def __init__(self,start):
        # Set variables for the game
        score = winnings = 0
        money = 1000
        center = Point(250,100)
        
        
        #quit_Button = Button(start, Point(50,140), 75, 25,15,"Quit", True)
        #p = win.getMouse()
        #while not quit_Button.clicked(p):
           # continue
        time.sleep(30)
        
        start.close()

        