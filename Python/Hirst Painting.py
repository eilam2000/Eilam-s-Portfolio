import turtle as t
import random
from turtle import Screen

color_list = [(233, 233, 236), (233, 232, 228), (236, 230, 233), (224, 234, 229), (176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117)]

tim = t.Turtle()
t.colormode(255)

tim.hideturtle()
start_x = -200
start_y = -200
tim.penup()
tim.goto(start_x, start_y)
tim.pendown()


def random_movement():
    for _ in range(100):
        random_color = random.choice(color_list)
        tim.color(random_color)
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()

        if _ % 10 == 9:  
            global start_y
            start_y += 50
            tim.penup()
            tim.goto(start_x, start_y)
            tim.pendown()

random_movement()






































screen = Screen()
screen.exitonclick()