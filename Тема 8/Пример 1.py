from itertools import product

count = 0
for p in product('ГЕПАРД', repeat=5):
    p = ''.join(p)
    if p.count('Г') == 1 and p[0] != 'А' and p[-1] != 'Е':
        count += 1
print(count)


# Версия II
count = 0
for p1 in 'ГЕПРД':
    for p2 in 'ГЕПАРД':
        for p3 in 'ГЕПАРД':
            for p4 in 'ГЕПАРД':
                for p5 in 'ГПАРД':
                    s = p1 + p2 + p3 + p4 + p5
                    if s.count('Г') == 1:
                        count += 1
print(count)


# Версия III
count = 0
for p in product('ГЕПРД', 'ГЕПАРД', 'ГЕПАРД', 'ГЕПАРД', 'ГПАРД'):
    p = ''.join(p)
    if p.count('Г') == 1:
        count += 1
print(count)