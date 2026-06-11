# Решение
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((x <= y) or (y == w)) and ((x or z) == w):
                    print(x, y, z, w)






answer = 'zxyw'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 27, answer, '9143f4e8bb70c861dcdb22bb9374e909'))