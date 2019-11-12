from hefunctions import *

turtle.bgcolor("pink")
turtle.colormode(255)
turtle.tracer(False)
bob=turtle.Turtle
turtle.speed(0)
turtle.shape("triangle")




for time in range(12):
    spikeFlower(36-time * 10)
    spike(200-time * 10)
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.right(time * 36)
turtle.tracer(True)
