"""
first graphics program.
need to have graphics.py in same directory, so we can import it.
for reference:
  https://www.cs.swarthmore.edu/courses/CS21Labs/f19/docs/graphics.html
"""

from graphics import *

def main():
    width = 500
    height = 400
    gw = GraphWin("my first graphics prog!", width, height)
    gw.setBackground("orange")

    # make a Point object
    x = width*.4
    y = height*.3
    cp = Point(x,y)

    # make a Circle object
    radius = width/20
    c = Circle(cp, radius)   # center is the Point obj
    c.setFill("black")
    c.draw(gw)

    # clone and move Circle to make another
    newc = c.clone()
    newc.move(width*.15,0)
    newc.draw(gw)

    # make a Line object
    p1 = Point(width*.3,height*.6)
    p2 = Point(width*.7,height*.6)
    l = Line(p1,p2)
    l.setWidth(4)
    l.draw(gw)

    # make a Text object
    p = Point(width*.5,height*.8)
    t = Text(p, "programming is fun!")
    t.draw(gw)

    # wait for mouse click, then program ends
    click = gw.getMouse()

main()
