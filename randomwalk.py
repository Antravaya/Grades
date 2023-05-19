from graphics import*
from math import pi, cos, sin
from random import random

def main():
    steps = 10000
    win = GraphWin("Random walk", 200, 200)
    p1 = Point(100,100)
    for i in range(steps):
        p2 = getNewRandomPoint(p1.getX(), p1.getY())
        drawLine(win, p1, p2)
        p1 = p2

        key = win.checkKey()
        if key == 'f':
            break

def getNewRandomPoint(x, y):
    angle = random() * 2 * pi
    x = x + cos(angle)
    y = y + sin(angle)
    return Point(x, y)

def drawLine(win, p1, p2):
    line = Line(p1, p2)
    line.draw(win)

if __name__ == "__main__": main()
