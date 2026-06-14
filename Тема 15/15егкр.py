lim = 2000000
for a in range(lim, 0, -1):
    if all((x*y < a) or (5*x < y) or (486 <= x) for x in range(0, lim) for y in range(0, lim)):
        print(a)
