# Решение
for x in range(0, 39):
    a = 1*39**0 + 7*39**1 + x*39**2 + 3*39**3 + 5*39**4 + 6*39**5
    b = 7*39**0 + 3*39**1 + x*39**2 + 2*39**3 + 4*39**4
    if (a+b) % 14 == 0:
        print(x, (a+b)/14)
        break






answer = 40176157

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1406, answer, '288e0c30469777cb2cfd847e9fb0f529'))