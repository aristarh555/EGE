# Решение
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((x == (not(y))) <= ((z <= (not(w))) and (w <= y))) == 0:
                    print(x, y, z, w)





answer = 'ywzx'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 25, answer, '1f3ba34df7bed082a628be303ad291df'))