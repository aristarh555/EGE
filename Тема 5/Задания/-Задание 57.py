# Решение
for n in range(10000000):
    bn = bin(n)[2:]
    l = list(str(n))
    s = 0
    for j in range(len(l)):
        s += int(l[j])
    if s % 2 == 0:
        bn = str(bn) + '0'
    else:
        bn = str(bn) + '1'
    l = list(str(bn))
    s = 0
    for j in range(len(l)):
        s += int(l[j])
    if s % 2 == 0:
        bn = str(bn) + '0'
    else:
        bn = str(bn) + '1'
    l = list(str(bn))
    s = 0
    for j in range(len(l)):
        s += int(l[j])
    if s % 2 == 0:
        bn = str(bn) + '0'
    else:
        bn = str(bn) + '1'
    r = int(bn, 2)
    if r > 1028:
        print(r)
        break









answer = 1032

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 57, answer, 'a34bacf839b923770b2c360eefa26748'))