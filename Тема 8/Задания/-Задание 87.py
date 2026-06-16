# Решение
from itertools import product

c = 0
for p in product('светлана', repeat=8):
    p = ''.join(p)
    if p.count('а') == 2 and p.count('с') == 1 and p.count('в') == 1 and p.count('е') == 1 and p.count('т') == 1 and p.count('л') == 1 and p.count('н') == 1 and p.count('аа') == 0 and p.count('сс') == 0 and p.count('вв') == 0 and p.count('ее') == 0 and p.count('тт') == 0 and p.count('лл') == 0 and p.count('нн') == 0:
        c += 1
print(c)






answer = 60480

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 87, answer, '590fcadab00abacc5caaf30b51e91ad3'))