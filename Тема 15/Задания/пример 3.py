p = range(-19826, 22713)
q = range(-11089, 185111)
min_len = 300000
for begin in range(300000):
    for end in range(300000):
        a = range(begin, end)
        if all((x in p) <= (((x in q) and (not(x in a))) <= (not(x in p))) for x in range(300000)):
            min_len = min(min_len, end - begin)
print(min_len)