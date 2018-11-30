# The program that executes the main functions of the game.
# Author: Qifu Yin
# Date: 12-27-2018

from graphics import *
import random
import sys
#from Deck import*
#from Button import*
#from Texts import*

class Deck:
    #This is a class for deck of playing card
    def __init__(self):
        self.soorten = ['h', 's', 'd','c']
        #'h' represents heart, 's' represents spade, 'd' represent diamond, 'c' represents club
        self.waarden = ['14','2','3','4','5','6','7','8','9','10','11','12','13']
        #11 represents 'J', 12 represents 'Q', 13 represents 'K', 14 represents 'A',

        #Create empty list
        self.deckofcards = list()
        self.shuffledcards = list()

        for suit in self.soorten:
            for num in self.waarden:
                kaart = suit + num
                self.deckofcards.append(kaart)

    #Create methond to shuffle the deck
    def Shuffle(self):
        self.shuffledcards = self.deckofcards
        random.shuffle(self.shuffledcards)
        return self.shuffledcards

    def Deal(self):
        card = self.shuffledcards.pop()
        return card

class Card(GraphicsObject):#subclass of GraphicsObject
    def __init__(self, win, value, center):
        self.value = value
        self.win = win
        self.centerPoint = center
        self.kaart = self.drawCard(value, center)
        self.kaart.draw(win)

    #Get the value of playing card
    def getValue(self):
        value = self.value[1:]
        return int(value)

    #Get suit of playing card
    def getSuit(self):
        color = self.value[0]
        return color

    def Undraw(self):
        self.kaart.undraw()

    def drawCard(self, value, center):
        self.center = center
        self.value = value
        file = "zhajinhua_cardgif/"+str(value)+ ".gif"
        self.image = Image(center,file)
        return Image(center, file)
