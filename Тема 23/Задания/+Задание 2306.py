# Решение
def f(x, y, k):
    if x == y:
        return 1
    if x > y:
        return 0
    if k == 1:
        return f(x+1, y, 0) + f(x*2, y,0)
    else:
        return f(x+1, y, 0) + f(x+2, y, 1) + f(x*2, y,0)

print(f(2, 22, 0))




answer = 4953

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2306, answer, '4ae1e2b07ecf6c799b91ed45e95278b8'))