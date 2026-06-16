# Решение

a = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 -6561
s = 0
while a > 0:
    if a % 27 > 9:
        s += 1
    a = a // 27
print(s)





answer = 3367

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1410, answer, '0e7e05fa1026b0c5459267608ae320b8'))