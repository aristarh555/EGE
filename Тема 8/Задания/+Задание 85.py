# Решение
from itertools import product
c = 1
for i in product('АГМНСТУ', repeat=6):
    i = ''.join(i)
    if i[0] != 'У' and i.count('М') == 2 and i.count('Г') <= 1:
        print(i, c)
    c += 1






answer = 100810

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 85, answer, '4f41663a6f277ab55c6b626aff28784a'))