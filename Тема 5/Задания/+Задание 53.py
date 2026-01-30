# Решение
def third(n):
    tn = ''
    while n > 0:
        tn = str(n % 3) + tn
        n //= 3
    return tn

for n in range(1000000):
    tr = third(n)
    if n % 3 == 0:
        tr = '1' + tr + '02'
    else:
        tr = tr + str(third((n%3)*4))
    r = int(tr, 3)
    if r <= 250:
        print(n)







answer = 26

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 53, answer, '4e732ced3463d06de0ca9a15b6153677'))