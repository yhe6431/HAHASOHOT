import turtle
turtle.colormode(255)
bob=turtle.Turtle()

def spikeFlower(distance):
    for times in range(11):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times*36)


def spike(distance):
    for times in range(20):
        C = times*12
        bob.color(C-times *12, C,C)
        bob.width(times*2)
        bob.forward(distance)
        bob.left(10)
 


def tile(c):
    polygon(4,200,c)
    for times in range(4):
        polygon(3,50,"orange")
        bob.forward(50)
        polygon(3,50,"blue")
        bob.forward(50)
        polygon(3,50,"green")
        bob.forward(50)
        polygon(3,50,"red")
        bob.forward(50)
        bob.left(90)

def rowtile(c):
    for times in range(8):
        tile(c)
        bob.forward(200)

def polygon(sides,distance,c):
    bob.color(c)
    angle = 360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)

    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance, c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(144)
    bob.end_fill()

def explosion(distance, C):
    bob.color(C)
    bob.begin_fill()
    for times in range(8):
        bob.forward(distance)
        bob.left(135)

    bob.end_fill()

def figure1(distance,size,color):
    bob.color(color)
    bob.begin_fill()
    bob.circle(size)
    bob.forward(distance)
    bob.circle(size)
    bob.left(75)
    bob.begin_fill()
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(45)
    bob.circle(size)
    bob.forward(distance)
    bob.circle(size)
    bob.end_fill()

def monster(color):
    bob.begin_fill()
    bob.color(color)
    bob.left(90)
    bob.forward(100)
    bob.circle(50)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(135)
    bob.forward(35)
    bob.right(90)
    bob.forward(35)
    bob.left(90)
    bob.forward(35)
    bob.right(90)
    bob.forward(35)
    bob.left(45)
    bob.end_fill()
    bob.left(45)

def fadingTriangle():
    for times in range(50):
        c=(250-times*5,250-times*5,0)
        polygon(3,450-times *8,c)

def baseball(distance):
    for times in range(14):
        bob.left(360-times*6)
