'''
from turtle import *


tracer(0)
x = 4
k = 10
for i in range(4):
    fd(x*k)
    rt(90)
    fd(x*k)
    lt(90)
    fd(x*k)
    rt(90)
pu()
for j in range(-50, 50):
    for c in range(-50, 50):
        goto(j*k, c*k)
        dot(3, 'red')
exitonclick()
'''
for x in range(1, 1000000):
    if 5*x**2 > 1000:
        print(x)
        break
