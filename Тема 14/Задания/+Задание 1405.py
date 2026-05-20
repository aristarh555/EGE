# Решение
for x in range(0, 22):
    a = 1 + 6*22 + 4*22**2 + x*22**3 + x*22**4 + 8*22**5 + 1*22**6 + 4*22**7 + 7*22**8 + 4 + x*22 + 5*22**2 + 2*22**3 + 6*22**4 + 9*22**5 + 1*22**6 + 7*22**7 + 9 + 9*22 + x*22**2 + 6*22**3 + 9*22**4 + 3*22**5
    if a % 21 == 0:
        print(a / 21)
        break






answer = 19614415862

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1405, answer, '04ffec330b9d276c1c81c59c1d1a4376'))