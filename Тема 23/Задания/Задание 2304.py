# Решение
def f(x, y, z):
    if x > y and z == 0:
        return 0
    if x > y + 1:
        return 0
    if x == y:
        return 1
    else:
        if z == 0:
            return f(x+3, y, 1) + f(x*2, y, 2)
        else:
            return f(x+3, y, 1) + f(x*2, y, 2) + f(x-1, y, 0)

print(f(3, 12, -1))





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2304, answer, 'd82c8d1619ad8176d665453cfb2e55f0'))