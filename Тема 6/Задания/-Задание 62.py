# Решение
from turtle import *
k=10
screensize(10000, 10000)
tracer(0)
rt(180)
for i in range(9):
    fd(59*k)
    lt(90)
    fd(84*k)
    lt(90)
pu()
fd(18*k)
lt(90)
fd(38*k)
lt(90)
pd()
for j in range(9):
    fd(120*k)
    rt(90)
    fd(99*k)
    rt(90)
pu()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(3, 'red')
exitonclick()





answer = 118

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 62, answer, '06409663226af2f3114485aa4e0a23b4'))