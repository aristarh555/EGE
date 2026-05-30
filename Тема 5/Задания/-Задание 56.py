# Решение
def f(n):
    b = bin(n)[2:]
    l = list(str(n))
    for i in range(len(l)):
        l[i] = int(l[i])
    s = sum(l)
    if s % 2 != 0:
        b += '1'
    if s % 2 == 0:
        b += '0'
    l = list(str(b))
    for i in range(len(l)):
        l[i] = int(l[i])
    s = sum(l)
    if s % 2 != 0:
        b += '1'
    if s % 2 == 0:
        b += '0'
    l = list(str(b))
    for i in range(len(l)):
        l[i] = int(l[i])
    s = sum(l)
    if s % 2 != 0:
        b += '1'
    if s % 2 == 0:
        b += '0'
    r = int(b, 2)
    return r

print(f(1987654321//8-1))
'''
start = 123456796
c = 1
while start <= 1987654318:
    start += 8
    c += 1
print(c)
'''


answer = 233024692

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 56, answer, 'f6e1eed3417f1dbf09acd31a21621ef3'))