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
        # Draw the bank and bet in the window
        bank_view = Scorebox(win, Point(115,20),"    $",money)
        bet_view = Scorebox(win, Point(210,20),"Bet:",bet)
        # Draw the buttons needed in the game
        draw_Button = Button(win, Point(50,40), 75, 25,15,"Draw", True)
        bet1_Button = Button(win, Point(50,65),75,25,15,"$1", False)
        bet5_Button = Button(win, Point(50,90),75,25,15,"$5", False)
        bet20_Button = Button(win, Point(50,115),75,25,15,"$20", False)
        bet50_Button = Button(win, Point(50,140),75,25,15,"$50", False)
        affirm_Button = Button(win, Point(50,165),75,25,15,"Affirm", False)
        again_Button = Button(win, Point(50,190), 75, 25,15,"Again", False)
        quit_Button = Button(win, Point(50,215), 75, 25,15,"Quit", True)
        buttons = [draw_Button,bet1_Button,bet5_Button,bet20_Button,bet50_Button,again_Button,quit_Button]
        # Create a deck and shuffle cards
        deck = Deck()
        deck.Shuffle()
        p = win.getMouse()
        # Begin the game
        while not quit_Button.clicked(p):
            p = win.getMouse()
            # User can click the draw button to start playing
            if draw_Button.clicked(p):
                # original bet
                bet = 1
                bet_view.updateText(bet)
                # draw 3 cards to player
                player_cards = []
                for i in range(3):
                    location = Point(125+25*i,90) # Place each card 25*i further on the x-axis
                    value = deck.Deal()
                    card = Card(win,value,location)
                    player_cards.append(card)
                 # draw 3 cards to computer
                computer_cards = []
                for i in range(3):
                    location = Point(125+25*i,200) # Place each card 25*i further on the x-axis
                    value = deck.Deal()
                    card = Card(win,value,location)
                    computer_cards.append(card)
                # update the bottons
                buttonUpdates('stillplaying',buttons) 
            if bet1_Button.clicked(p):
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    
    
    
