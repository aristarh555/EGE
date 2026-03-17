# Решение
for x in range(7):
    for y in range(7):
        p1 = 0 + 2*7**1 + 3*7**2 + x*7**3 + y*7**4
        p2 = 3 + y*9**1 + 3*9**2 + x*9**3 + 1*9**4
        r = p1 + p2
        if r % 181 == 0:
            print(r/181)
            break






answer = 148

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1402, answer, '47d1e990583c9c67424d369f3414728e'))