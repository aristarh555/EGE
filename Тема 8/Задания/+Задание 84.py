# Решение
from itertools import product

c = 0
for p in product('0123456789ABCDEF', repeat=6):
    p = ''.join(p)
    p = p.replace('DD', '*').replace('EE', '*').replace('FF', '*').replace('DE', '*').replace('ED', '*').replace('DF', '*').replace('FD', '*').replace('EF', '*').replace('FE', '*')
    if p.count('5') >= 1 and p.count('D') == 0 and p.count('E') == 0 and p.count('F') == 0 and p.count('*') == 1 and p[0] != '0':
        c += 1
print(c)






answer = 335241

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 84, answer, '85705f54f8b912d25a2eac2583e7093d'))