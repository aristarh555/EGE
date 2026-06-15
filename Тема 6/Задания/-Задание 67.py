# Решение
from turtle import *

tracer(0)
rt(90)
k=30
for i in range(4):
    fd(4*(5**0.5)*k)
    rt(150)
    fd(4 * (5 ** 0.5) * k)
    rt(300)
pu()
for x in range(-50, 100):
    for y in range(-50, 100):
        goto(x*k, y*k)
        dot(3, 'red')
exitonclick()









answer = 87

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 67, answer, 'ac627ab1ccbdb62ec96e702f07f6425b'))