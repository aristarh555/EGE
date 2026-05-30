# Решение
def f(n):
    b = bin(n)[2:]
    b += bin(n % 4)[2:]
    r = int(b, 2)
    return r
for i in range(1, 1000):
    print(f(i), f(i)//i)





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 54, answer, '473b677ddfbedbb3d2e6d5e5980dc6e1'))