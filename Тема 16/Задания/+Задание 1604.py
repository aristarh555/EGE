# Решение
def f(n):
    if n < 3:
        return 1
    if n % 2 != 0 and n > 2:
        return f(n-1) + 3*f(n-2)
    if n % 2 == 0 and n > 2:
        return sum(f(i) for i in range(1, n))
print(f(28))






answer = 814893696

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1604, answer, 'e31a2673da538481c8408e028f67a70a'))