# Решение
import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n < 4000:
        return n
    if n % 7 == 0 and n >= 4000:
        return n + f(n/7)
    if n % 7 != 0 and n >= 4000:
        return 567 + f(n-3)
for i in range(0, 100000):
    if f(i) > 80000:
        print(i)
        break







answer = 62962

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1606, answer, 'c664ec48cfb940b2ce2386c8fb7f9be8'))