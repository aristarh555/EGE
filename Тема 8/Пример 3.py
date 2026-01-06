from itertools import permutations
count = 0
for p in permutations('МАТВЕЙ', 6):
    p = ''.join(p)
    if p[0] != 'Й' and p.count('АЕ') == 0:
        count += 1
print(count)