for n in range(1, 100000000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = str(r) + '0'
    print(r)