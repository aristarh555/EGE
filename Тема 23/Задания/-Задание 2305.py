# Решение
def f(x, y):
    if x == y:
        return 1
    if x > y or x == 8:
        return 0
    return f(x+1, y) + f(x+2, y) + f(x*2, y)
print(f(3, 14) + f(14, 18))







answer = 77

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2305, answer, 'e7b24b112a44fdd9ee93bdf998c6ca0e'))