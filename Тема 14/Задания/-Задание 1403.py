# Решение
a = 3*3125**8 + 2*625**7 + 4*625**6 + 3*125**5 - 2*25**4 - 2024
s = 0
while a > 0:
    if a % 25 == 0:
        s += 1
    a = a // 25
print(s)







answer = 10

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1403, answer, '45c48cce2e2d7fbdea1afc51c7c6ad26'))