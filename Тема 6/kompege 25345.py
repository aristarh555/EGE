from turtle import *
tracer(0)
koef = 20
x = 3
for i in range(6):
    forward(33 * koef)
    right(90)
    forward(20 * koef)
    right(90)
up()
forward(3 * koef)
right(90)
forward(9 * koef)
left(90)
down()
for i in range(6):
    forward(24 * koef)
    right(90)
    forward(25 * koef)
    right(90)
up()
for x in range(-koef * 2, koef * 2):
    for y in range(-koef * 2, koef * 2):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()