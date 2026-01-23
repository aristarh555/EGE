from itertools import product

count = 0
for p in product('0123456789AB', repeat=6):
    if p.count('7')==1 and p[0] != '0' and p.count('A') + p.count('B') <= 3:
        count += 1
print(count)
