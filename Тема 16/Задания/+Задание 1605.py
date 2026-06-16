# Решение
import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n <= 10:
        return n
    if n > 10:
        return n-7 + f(n-21)
print((f(185734) -f(185650))/f(40))







answer = 17274

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1605, answer, 'ff413935bfae4f0e2d8dce0e0dacfdcd'))