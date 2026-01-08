# Решение
from itertools import product

count = 0
for p in product('ГЕПАРД', repeat=5):
    p = ''.join(p)
    if p.count('Г') == 1 and p[0] != 'А' and p[-1] != 'Е':
        count += 1
print(count)






answer = 2200

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 8, answer, '5249ee8e0cff02ad6b4cc0ee0e50b7d1'))