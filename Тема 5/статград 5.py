for n in range(1, 100000000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '1' + r[1:-1] + '0'
    else:
        r = '11' + r[1:-1] + '1'
    r = int(r, 2)
    if r < 744:
        print(r)