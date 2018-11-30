# The program that executes the main functions of the game.
# Author: Qifu Yin
# Date: 12-27-2018

from graphics import *
import time
import random
import time
import sys
#from Deck import*
from Button import*
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
        score = 0
        money = 100
        center = Point(250,100)
        
        # Draw the buttons needed in the game
        draw_Button = Button(start, Point(50,40), 75, 25,15,"Draw", True)
        bet_Button = Button(start, Point(50,65),75,25,15,"Bet", False)
        #pass_Button = Button(win, Point(50,90),75,25,15,"Pass", False)
        again_Button = Button(start, Point(50,115), 75, 25,15,"Again", False)
        quit_Button = Button(start, Point(50,140), 75, 25,15,"Quit", True)
        #newdeck_Button = Button(win, Point(112,33), 50, 12,10,"New deck", False)
        buttons = [draw_Button,bet_Button,again_Button,again_Button,quit_Button]
          # Create a deck and shuffle it 3 times
        deck = Deck()
        for i in range(3):
            deck.Shuffle()

        p = win.getMouse()
        totalCards = 0


        #quit_Button = Button(start, Point(50,140), 75, 25,15,"Quit", True)
        #p = win.getMouse()
        #while not quit_Button.clicked(p):
           # continue
        time.sleep(30)

        start.close()
