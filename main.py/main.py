import turtle

pen = turtle.Turtle()

def curve ():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140) 
    pen.forward()
    curve()
    pen.forward(112)
    pen.end_fill()

def text():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('yellow')
    pen.write("VAI TOMA NO CU")

    heart()
    text()
    pen.ht()


