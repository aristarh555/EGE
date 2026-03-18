# Решение
k = 0
for n in range(100000000,9999999999):
    bn = bin(n)[2:]
    n4 = bin(n % 4)[2:]
    r = int(str(bn) + str(n4), 2)
    print(r)





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 54, answer, '473b677ddfbedbb3d2e6d5e5980dc6e1'))