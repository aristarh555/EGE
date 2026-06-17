# Решение
for n in range(2, 1000000):
    bn = bin(n)[2:]
    if bn.count('1') % 2 == 0:
        bn = bn.replace(bn[0], '1')
        bn = bn.replace(bn[1], '0')
        bn += ('0')
    if bn.count('1') % 2 != 0:
        bn = bn.replace(bn[0], '1')
        bn = bn.replace(bn[1], '1')
        bn += ('1')
    r = int(bn, 2)
    if r <= 19 and r != 0:
        print(n, r)








answer = 9

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 510, answer, 'c20ad4d76fe97759aa27a0c99bff6710'))