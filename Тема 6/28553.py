from turtle import *
tracer(0)
screensize(5000, 5000)
koef = 15

rt(90)
for _ in range(17):
    fd(koef * 80)
    lt(90)
    fd(koef * 125)
    lt(90)
up()

fd(koef * 45)
lt(90)
fd(koef * 28)
lt(90)

down()

for _ in range(20):
    fd(koef * 160)
    rt(90)
    fd(koef * 150)
    rt(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()