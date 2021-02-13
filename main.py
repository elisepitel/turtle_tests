import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

franklin = Turtle()
screen = Screen()

franklin.shape("turtle")
franklin.color("forest green")


#for _ in range(4):
#    franklin.forward(100)
#    franklin.right(90)

#for _ in range(4):
#    for _ in range(10):
#        franklin.forward(10)
#        franklin.penup()
#        franklin.forward(10)
#        franklin.pendown()
#    franklin.right(90)



#screen.colormode(255)
#def draw_shape(num_side):
#    degree = int(360 / num_side)
#    for move in range(num_side):
#        franklin.forward(100)
#        franklin.right(degree)
#for shape_side_n in range(3, 11):
#    var_R = random.randrange(0, 257, 10)
#    var_G = random.randrange(0, 257, 10)
#    var_B = random.randrange(0, 257, 10)
#    franklin.pencolor(var_R, var_G, var_B)
#    draw_shape(shape_side_n)


## Random Walk:
#franklin.pensize(7)
#franklin.speed(9)
#
#
#def turn_randomly():
#    degrees = [0, 90, 180, 270]
#    franklin.setheading(random.choice(degrees))
#    franklin.forward(20)
#
#
#def random_color():
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    color_tuple = (r, g, b)
#    return color_tuple
#
#
#for _ in range(250):
#    franklin.pencolor(random_color())
#    turn_randomly()


## Spirograph
franklin.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        franklin.color(random_color())
        franklin.circle(150)
        franklin.setheading(franklin.heading() + size_of_gap)


draw_spirograph(2.5)


screen.exitonclick()
