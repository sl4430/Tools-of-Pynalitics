# The program that executes the main functions of the game.
# Author: Qifu Yin
# Date: 12-27-2018

from graphics import *
import time
import random
import time
import sys
#from Deck import*
#from Button import*
#from Texts import*

class Game():
    def __init__(self):
        #set the main background for the game
        start = GraphWin("zhajinhua", 700, 400)
        start.setCoords(0,400,615,0)
        start.setBackground("white")
        table = Rectangle(Point(600,353),Point(87,27))
        table.setFill("brown")
        table.draw(start)
        # Set variables for the game
        score = winnings = 0
        money = 1000
        center = Point(250,100)
        # Set variables for the game
        bet = 0
        money = 1000
        center = Point(250,100)

        #p = win.getMouse()
        #while not quit_Button.clicked(p):
           # continue
        time.sleep(30)

        start.close()
