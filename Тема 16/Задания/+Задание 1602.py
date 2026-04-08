# Решение
'''
def f(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return f(n-1) + 1
    elif n % 2 == 0 and n > 0:
        return f(n//2)
for i in range(0, 100):
    print(i , '-', f(i))

c = 0
for n in range(0, 1000000000):
    if f(n) == 2:
        c += 1
print(c)
'''
'''
limit = 1000000000
dp = [0]*limit
for n in range(0, limit):
    if n == 0:
        dp[n] = 0
    elif n % 2 != 0:
        dp[n] = dp[n-1] + 1
    elif n % 2 == 0 and n > 0:
        dp[n] = dp[n//2]
c = 0
for i in range(limit):
    if dp[i] == 2:
        c += 1
print(c)
'''
'''
c = 0
for i in range(0, 1000000000):
    if bin(i).count('1') == 2:
        c += 1
print(c)
'''



answer = 435

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1602, answer, 'ddb30680a691d157187ee1cf9e896d03'))