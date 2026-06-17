# Решение
for n in range(1, 10000000):
    bn = bin(n)[2:]
    for j in range(3):
        l = list(str(int(bn, 2)))
        s = 0
        for i in range(len(l)):
            s += int(l[i])
        if s % 2 != 0:
            bn += '1'
        elif s % 2 == 0:
            bn += '0'
    r = int(bn, 2)
    if r > 1028:
        print(r)
        break











answer = 1035

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 57, answer, 'a34bacf839b923770b2c360eefa26748'))