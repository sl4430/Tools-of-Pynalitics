# the main program starts the game and executes the Game class.
# Author: Qifu Yin, Shujun Liu, Shixin Li, Di Zhu
# Date: 12-02-2018

#Run this file to start game
from graphics import *
from Game import *
    
def main():
    winStart = GraphWin("Zhajinhua", 800, 400)
    winStart.setCoords(0,250,415,0)
    winStart.setBackground("grey")

    # Draw the table
    table = Rectangle(Point(400,225),Point(87,30))
    table.setFill("white")
    table.draw(winStart)
    

    Game(winStart)

    winStart.close()

if __name__ == "__main__":
    main()