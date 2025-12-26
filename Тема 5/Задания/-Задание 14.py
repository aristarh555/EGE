# Решение
k = 0
x = 5
y = 55
for n in range(x, y):
    bn = bin(n)[2:]
    bn = str(bn) + str(bin(n%4)[2:])
    r = int(bn, 2)
    if r >= x and r <= y:
        k += 1
print(k)







answer = 18

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 14, answer, '1f0e3dad99908345f7439f8ffabdffc4'))