from turtle import *
tracer(0)
koef = 30

for _ in range(2):
    forward(8 * koef)
    left(270)
    backward(6 * koef)
    right(90)

up()

forward(5 * koef)
right(90)
backward(3 * koef)
left(90)

down()

for _ in range(2):
    forward(7 * koef)
    right(90)
    forward(2 * koef)
    right(90)

up()

forward(3 * koef)
right(180)
backward(1 * koef)

down()

for _ in range(2):
    forward(5 * koef)
    right(90)
    forward(5 * koef)
    right(90)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()