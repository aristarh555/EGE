from itertools import product


c = 0
for p in product('ио', 'вкрт', 'ио', 'вкрт'):
    if p.count('и') <= 1 and p.count('о') <= 1 and p.count('в') <= 1 and p.count('к') <= 1 and p.count('р') <= 1 and p.count('т') <= 1:
        c += 1
for p in product('вкрт', 'ио', 'вкрт', 'ио'):
    if p.count('и') <= 1 and p.count('о') <= 1 and p.count('в') <= 1 and p.count('к') <= 1 and p.count('р') <= 1 and p.count('т') <= 1:
        c += 1
print(c)
