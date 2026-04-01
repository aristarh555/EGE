# Решение


def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)

# Путь: 3 -> 9 -> 14
print(f(9, 24) * f(24, 81))
print(f(9, 27) * f(27, 81))





answer = 222

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2301, answer, 'a8baa56554f96369ab93e4f3bb068c22'))