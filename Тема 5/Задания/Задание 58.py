# Решение
for n in range(100000, 100000000000):
    n = 2021
    sum1 = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            sum1 += int(digit)
    sum2 = 0
    for i in range(1, len(str(n)), 2):
        sum2 += int(str(n)[i])
    r = abs(sum1 - sum2)
    if r == 13:
        print(n)
        break







answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 58, answer, 'eb6fdc36b281b7d5eabf33396c2683a2'))