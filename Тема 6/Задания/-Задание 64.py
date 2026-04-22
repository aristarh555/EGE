# Решение
from turtle import *
k = 10
tracer(0)

for i in range(2):
    fd(15*k)
    rt(90)
    fd(8*k)
    rt(90)
pu()
for x in range(-20, 100):
    for y in range(-20, 100):
        goto(x*k, y*k)
        dot(3, 'red')
exitonclick()




answer = 49

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 64, answer, '9f61408e3afb633e50cdf1b20de6f466'))