# Решение
from turtle import *

tracer(0)
k = 20
for i in range(4):
    fd(9*k)
    rt(90)
for i in range(3):
    fd(9*k)
    rt(120)
pu()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(3, 'red')
exitonclick()






answer = 33

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 66, answer, 'e369853df766fa44e1ed0ff613f563bd'))