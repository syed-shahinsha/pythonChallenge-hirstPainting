import turtle as t
import random

color_list = [(226, 226, 225), (182, 65, 34), (213, 149, 97), (14, 24, 42), (230, 237, 233), (239, 208, 94), (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115), (166, 141, 66), (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127), (229, 175, 161), (165, 64, 70)]

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')


def create_painting(rows_x_cols, space_between_dots):
    col_y = 0
    tim.penup()

    for row in range(rows_x_cols):
        for col in range(rows_x_cols):
            tim.dot(20, random.choice(color_list))
            tim.forward(space_between_dots)
        col_y += space_between_dots
        tim.sety(col_y)
        tim.setx(0)


# rows_x_cols signifies how many rows and columns needs to be there in the painting
create_painting(rows_x_cols=7, space_between_dots=30)

screen = t.Screen()
screen.exitonclick()
