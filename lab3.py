# Lab No. 3
# CTEC 121
# Sean Mcilvenny

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    circle1 = Circle(Point(400,220),75)
    circle1.draw(win)
    circle2 = Circle(Point(400,380),100)
    circle2.draw(win)
    circle3 = Circle(Point(400,625),150)
    circle3.draw(win)

    button1 = Circle(Point(398,323),10)
    button1.setFill('black')
    button1.draw(win)
    button2 = Circle(Point(398,380),10)
    button2.setFill('black')
    button2.draw(win)
    button3 = Circle(Point(398,441),10)
    button3.setFill('black')
    button3.draw(win)




    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    eye1 = Circle(Point(360,200),15)
    eye1.setFill('black')
    eye1.draw(win)
    eye2 =eye1.clone()
    eye2.move(80,0)
    eye2.setFill('black')
    eye2.draw(win)



    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose

    nose = Polygon(Point(393,224),Point(365,262),Point(416,242))
    nose.setFill('orange')
    nose.draw(win)


    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat

    hat = Rectangle(Point(360,136),Point(446,89))
    hat.setFill('black')
    hat.draw(win)




    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline

    hatLine = Line(Point(304,140),Point(505,140))
    hatLine.setWidth(10)
    hatLine.draw(win)

    # for i in range(3):
    #     point = win.getMouse()
    #     x = point.getX()
    #     y = point.getY()

    #     print(x,y)




    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()