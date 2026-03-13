def f(n):
    p = 1
    temp = n
    max_n = -1
    min_n = 10
    while temp > 0:
        digit = temp % 10
        max_n = max(digit, max_n)
        min_n = min(min_n, digit)
        if digit > 0:
            p *= digit
        temp //= 10
    m = max_n + min_n
    t1 = p + m
    t2 = p * m
    if t1 > t2:
        return int(str(t2) + str(t1))
    else:
        return int(str(t1) + str(t2))

for n in range(1, 10000000):
    if f(n) == 23126:
        print(n)