
# the main program starts the game.
# Author: Qifu Yin, Shujun Liu, Shixin Li, Di Zhu
# Date: 12-02-2018

#Use this as the main script
from graphics import *
from Game import *

       
def main():
    win = GraphWin("Zhajinhua", 800, 400)
    win.setCoords(0,250,415,0)
    win.setBackground("grey")

    # Draw the table
    table = Rectangle(Point(400,153),Point(87,27))
    table.setFill("brown")
    table.draw(win)

    Game(win)

    win.close()

if __name__ == "__main__":
    main()