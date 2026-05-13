# Решение
import sys
sys.setrecursionlimit(10**8)
def f(n):
    if n == 0:
        return 0
    else:
        return f(n // 10) + f(n % 10)
c = 0
for n in range(765432015, 1542613239):
    if f(n) > f(n+1):
        c += 1
print(c)







answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1603, answer, '383d228fc45e55c06236b5d6278e1765'))