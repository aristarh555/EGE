# Решение
import turtle

t = turtle.tracer(0)
k = 30
for i in range(2):
    turtle.fd(3*k)
    turtle.lt(90)
    turtle.bk(10*k)
    turtle.lt(90)
turtle.pu()
turtle.bk(10 * k)
turtle.rt(90)
turtle.fd(8 * k)
turtle.lt(90)
turtle.pd()
for j in range(2):
    turtle.fd(16*k)
    turtle.rt(90)
    turtle.fd(8*k)
    turtle.rt(90)
turtle.pu()
for x in range(-k, k):
    for y in range(-k, k):
        turtle.goto(x*k, y*k)
        turtle.dot(3)
turtle.exitonclick()








answer = 185

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 6, answer, 'eecca5b6365d9607ee5a9d336962c534'))