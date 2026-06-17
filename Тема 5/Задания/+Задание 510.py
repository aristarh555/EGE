# Решение
for n in range(2, 1000000):
    bn = bin(n)[2:]
    if bn.count('1') % 2 == 0:
        bn = '10' + bn[2:] + '0'
    elif bn.count('1') % 2 != 0:
        bn = '11' + bn[2:] + '1'
    r = int(bn, 2)
    if r <= 19:
        print(n, r)









answer = 12

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 510, answer, 'c20ad4d76fe97759aa27a0c99bff6710'))