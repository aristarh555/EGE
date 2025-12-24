# Решение
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (((x == y) <= (not(z) or w)) == (not((w<=x) or (y <= z)))) == 1:
                    print(x, y, z, w)







answer = 'yzxw'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 2, answer, 'e0abee87e4ba1de22c6b8cf076c5016b'))