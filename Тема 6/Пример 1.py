
from turtle import *
tracer(0)
koef = 20
x = 3
for i in range(5):
    forward(x * koef)
    right(90)
    forward(3 * koef)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()

x = 1
while True:
    if (x + 4) ** 2 > 400:
        print(x)
        break
    x += 1