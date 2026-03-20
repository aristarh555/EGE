'''
import functools
functools.lru_cache(maxsize=None)
def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return f(n//10) + n % 10
    elif n % 2 != 0:
        return f(n//10)
k = 0
for n in range(10**7, 6*10**7 + 1):
    if f(n) == 0:
        k += 1
print(k)
'''
limit = 6*10**7
dp = [0]*(limit+2)
for n in range(limit+1):
    if n == 0:
        dp[n] = 0
    elif n % 2 == 0 and n > 0:
        dp[n] = dp[n//10] + n % 10
    elif n % 2 != 0 and n >= 0:
        dp[n] = dp[n//10]
k = 0
for i in range(10**7, limit+1):
    if dp[i] == 0:
        k += 1
print(k)
