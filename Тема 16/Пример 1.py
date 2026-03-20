def F(n):
    if n < 5000:
        return n
    elif n >= 5000 and n % 5 == 0:
        return n + F(n/5)
    elif n >= 5000 and n % 5 != 0:
        return 117 + F(n-3)
for i in range(-100, 1000000):
    if F(i) > 100000:
        print(i)
        break