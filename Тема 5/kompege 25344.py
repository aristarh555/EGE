def to_ternary(n):
    res = ''
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res

def f(n):
    b = to_ternary(n)
    if n % 3 == 0:
        b += b[-2:]
    else:
        s = b.count('1') + b.count('2') * 2
        b += to_ternary(s * 3)
    return int(b, 3)

n = 1
while True:
    r = f(n)
    if r > 208 and r % 2 != 0:
        print(r)
        break
    n += 1

