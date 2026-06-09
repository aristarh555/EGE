# Решение
from turtle import *
tracer(0)
k = 10
x = 9
fd((x+2)*k)
for i in range(4):
    fd(x*k)
    rt(90)
    fd((x+2)*k)
rt(90)
fd(2*x*k)
for j in range(4):
    rt(90)
    fd(k*(3*x - 1))
pu()
for x in range(-50, 100):
    for y in range(-50, 100):
        goto(x*k, y*k)
        dot(3, 'red')
for x in range (0, 1000):
    if (x + x + 2)**2 + (3 * x - 1)**2 - (x + 2) * (2 * x) > 2000:
        print (x)
        break

exitonclick()






answer = 14

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 61, answer, 'aab3238922bcc25a6f606eb525ffdc56'))