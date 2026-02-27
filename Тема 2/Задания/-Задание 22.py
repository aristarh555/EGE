# Решение
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (not(x) and (not(y)) and (not(w)) and z) or (not(x) and z and y and (not(w))) or (not(x) and z and y and w):
                    print(x, y, z, w)






answer = 'xywz'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 22, answer, 'c5e4e768af58cf865c4006af69319e62'))