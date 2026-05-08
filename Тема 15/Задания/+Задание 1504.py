# Решение


for a in range(500):
    if all((y > a) or (152 != 2*y + 3*x) or (a < x) for x in range(400) for y in range(400)):
        print(a)





answer = 30

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1504, answer, '34173cb38f07f89ddbebc2ac9128303f'))