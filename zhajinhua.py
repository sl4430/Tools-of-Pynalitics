
# the main program starts the game and Creates the main background.
# Author: Qifu Yin
# Date: 12-27-2018

from graphics import *
from Game import *

       
def main():
    start = GraphWin("zhajinhua", 700, 400)
    start.setCoords(0,400,615,0)
    start.setBackground("white")

    # set the main background
    table = Rectangle(Point(600,353),Point(87,27))
    table.setFill("brown")
    table.draw(start)
    #call the game.py
    Game(start)

    start.close()
#check if the program should terminate
if __name__ == "__main__":
    main()
