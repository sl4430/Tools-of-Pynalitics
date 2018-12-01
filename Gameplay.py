# The program that executes the main functions of the game.
# Author: Qifu Yin
# Date: 12-27-2018

from graphics import *
import time
import random
import time
import sys
from Deck import*
from Button import*
from Texts import*

class Game():
    def __init__(self,win):
        #set the main background for the game
#         start = GraphWin("zhajinhua", 700, 400)
#         start.setCoords(0,400,615,0)
#         start.setBackground("white")
#         table = Rectangle(Point(600,353),Point(87,27))
#         table.setFill("brown")
#         table.draw(start)
        # Set variables for the game
        bet = 0
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
        buttons = [draw_Button,bet1_Button,bet5_Button,bet20_Button,bet50_Button,affirm_Button,again_Button,quit_Button]
        # Create a deck and shuffle cards
        deck = Deck()
        deck.Shuffle()
        p = win.getMouse()
        
        # Begin the game:
        
        while not quit_Button.clicked(p):
            p = win.getMouse()
            # User can click the draw button to start playing
            if draw_Button.clicked(p):
                # view original bet
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
                    location = Point(300+25*i,90) # Place each card 25*i further on the x-axis
                    value = deck.Deal()
                    card = Card(win,value,location)
                    computer_cards.append(card)
                    card.Undraw()
                # update the bottons
                buttonUpdates('stillplaying',buttons) 
            if bet1_Button.clicked(p):
                bet += 1
                bet_view.updateText(bet)
            if bet5_Button.clicked(p):
                bet += 5
                bet_view.updateText(bet)
            if bet20_Button.clicked(p):
                bet += 20
                bet_view.updateText(bet)
            if bet50_Button.clicked(p):
                bet += 50
                bet_view.updateText(bet)
            if affirm_Button.clicked(p):
                # compare the cards to decide who wins and settlement
                if compare(player_cards, computer_cards):
                    money += bet
                    bank_view.updateText(money)
                else:
                    money -= bet
                    bank_view.updateText(money)
                # Draw the computer cards
                for card in computer_cards:
                    card.kaart.draw(win)
                # update the buttons
                buttonUpdates('gameover',buttons)
            if again_Button.clicked(p):
                # clear the cards
                for i in player_cards:
                    i.Undraw()
                for i in computer_cards:
                    i.Undraw()
                # reset the scoreboard
                bet = 0
                bet_view.updateText(bet)
                # update the buttons
                buttonUpdates("newgame", buttons)
                deck = Deck()
                deck.Shuffle()
                
        # Window closes if the quit_Button is clicked
        win.close()
        
def is_bomb(cards):
    value = []
    for card in cards:
        value.append(card.value[1:])
    if value[0] == value[1] and value[1] == value[2]:
        return True
    return False
def is_sf(cards):
    suit = []
    value = []
    for card in cards:
        suit.append(card.value[0])
        value.append(int(card.value[1:]))
    if suit[0] == suit[1] and suit[1] == suit[2]:
        if '14' in value:
            if '12' in value:
                if '13' in value:
                    return True
            return False
        else:
            value = sorted(value)
            if abs(value[0]-value[1]) == 1 and abs(value[1]-value[2]) == 1:
                return True
            else:
                return False
def is_flush(cards):
    suit = []
    for card in cards:
        suit.append(card.value[0])
    if suit[0] == suit[1] and suit[1] == suit[2]:
        return True
    return False
def is_straight(cards):
    value = []
    for card in cards:
        value.append(int(card.value[1:]))
    if '14' in value:
        if '12' in value:
            if '13' in value:
                return True
        return False
    else:
        value = sorted(value)
        if abs(value[0]-value[1]) == 1 and abs(value[1]-value[2]) == 1:
            return True
        else:
            return False
    
def is_pair(cards):
    value = []
    for card in cards:
        value.append(card.value[1:])
    if value[0] == value[1] or value[0] == value[2] or value[2] == value[1]:
        return True
    return False

def get_max(cards):
    #get the type of hands, 6 is bomb and 1 is single
    if is_bomb(cards):
        return 6
    elif is_sf(cards):
        return 5
    elif is_flush(cards):
        return 4
    elif is_straight(cards):
        return 3
    elif is_pair(cards):
        return 2
    else:
        return 1

def compare(cards1, cards2):
    # cards1 is player and cards2 is computer
    number_1 = get_max(cards1)
    number_2 = get_max(cards2)
    suit1 = suit2 = []
    value1 = value2 = []
    for card in cards1:
        suit1.append(card.value[0])
        value1.append(int(card.value[1:]))
    for card in cards2:
        suit2.append(card.value[0])
        value2.append(int(card.value[1:]))
    # if num1 > num2, player wins, return True
    if number_1 > number_2:
        return True
    # if num1 > num2, computer wins, return False
    elif number_1 < number_2:
        return False
    # same type of hands
    elif number_1 == number_2:
        # if bomb
        if number_1 == 6:
            if value1[0] >= value2[0]:
                return True
            return False
        # if sf and straight
        if number_1 == 5 or number_1 == 3:
            max1 = max(value1)
            max2 = max(value2)
            if max1 >= max2:
                return True
            return False
        # if flush and single
        if number_1 == 4 or number_1 == 1:
            value1 = sorted(value1,reverse = True)
            value2 = sorted(value2,reverse = True)
            if value1[0] > value2[0]:
                return True
            elif value1[0] < value2[0]:
                return False
            elif value1[0] == value2[0]:
                if value1[1] > value2[1]:
                    return True
                elif value1[1] < value2[1]:
                    return False
                elif value1[1] == value2[1]:
                    if value1[2] >= value2[2]:
                        return True
                    else:
                        return False
        # if pair
        if number_1 == 2:
            value1 = sorted(value1)
            value2 = sorted(value2)
            if value1[0] == value1[1]:
                pair_value1 = value1[0]
                single_value1 = value1[2]
            else:
                pair_value1 = value1[2]
                single_value1 = value1[0]
            if value2[0] == value2[1]:
                pair_value2 = value2[0]
                single_value2 = value2[2]
            else:
                pair_value2 = value2[2]
                single_value2 = value2[0]
            if pair_value1 > pair_value2:
                return True
            elif pair_value1 < pair_value2:
                return False
            else:
                if single_value1 >= single_value2:
                    return True
                else:
                    return False

            
            
        









        

           
