# Решение
for n in range(2, 1000000):
    r = bin(n)[2:]
    c = r[0::2].count('0')
    k = r[1::2].count('1')
    '''
    c = 0
    k = 0
    for i in range(len(r)):
        if i % 2 == 0 and r[i] == '0':
            c += 1
        if i % 2 != 0 and r[i] == '1':
            k += 1
    '''
    r = abs(c - k)
    if r == 5:
        print(n)
        break

answer = 1023

#

from tests.conftest import result_register

if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))
