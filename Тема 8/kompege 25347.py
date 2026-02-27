from itertools import product

i = 1
for line in product('АГИНРТ', repeat=6):
    line = "".join(line)
    if line[0] not in 'АИГ' and line.count('А') == 1 and i % 2 != 0:
        print(i)
        break
    i += 1

