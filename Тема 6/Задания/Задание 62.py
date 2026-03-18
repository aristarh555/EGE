# Решение
from turtle import *
k=1
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
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x, y)
        dot(3, 'red')





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 62, answer, '06409663226af2f3114485aa4e0a23b4'))