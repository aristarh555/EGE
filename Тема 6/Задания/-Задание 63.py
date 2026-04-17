# Решение
from turtle import *
tracer(0)
k = 10
screensize(2080, 2080)
for i in range(7):
    fd(17*k)
    rt(90)
    fd(26*k)
    rt(90)
pu()
fd(4*k)
rt(90)
fd(6*k)
lt(90)
pd()
for i in range(7):
    fd(278*k)
    rt(90)
    fd(345*k)
    rt(90)
pu()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(3, 'red')

exitonclick()






answer = 96098

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 63, answer, '35495f83adcdab84ab446b313a3e0cb4'))