# Решение
for n in range(2, 1000000):
    n = 39
    r = bin(n)[2:]
    c = 0
    for i in range(len(r)):
        if i % 2 == 0 and r[i] == '1':
            c += 1
    k = 0
    for j in range(len(r)):
        if j % 2 != 0 and r[j] == '0':
            k += 1
    r = abs(c-k)
    if r == 5:
        print(n)
        break






answer = 511

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))