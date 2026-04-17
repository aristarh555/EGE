# Решение
from turtle import *
tracer(-1)
k = 5
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
for x in range(0, 350):
    for y in range(0, 350):
        goto(x*k, y*k)
        dot(3, 'red')






answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 63, answer, '35495f83adcdab84ab446b313a3e0cb4'))