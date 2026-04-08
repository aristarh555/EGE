# Решение

def f(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return f(n-1) + 1
    elif n % 2 == 0 and n > 0:
        return f(n/2)
c = 0
n = 0
while n < 1000000000:
    if f(n) == 2:
        c += 1
    n+=1
print(c)






answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1602, answer, 'ddb30680a691d157187ee1cf9e896d03'))