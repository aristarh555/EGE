# Решение
from turtle import *


k = 20
tracer(0)
rt(270)
for i in range(2):
    fd(8*k)
    rt(120)
rt(120)
for j in range(2):
    rt(120)
    fd(3*k)
    rt(240)
rt(240)
for z in range(2):
    fd(14*k)
    rt(120)
pu()
for x in range(-50, 100):
    for y in range(-50, 100):
        goto(x*k, y*k)
        dot(3, 'red')
exitonclick()






answer = 84

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 68, answer, '68d30a9594728bc39aa24be94b319d21'))