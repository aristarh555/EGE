# Решение
lst = [0] * 10000

for n in range(1, 1000):
    bn = bin(n)[2:]
    bn = str(bn) + str(bin(n%4)[2:])
    r = int(bn, 2)
    lst[r] = 1
m = 0
for i in range(len(lst)-49):
    m = max(m, lst[i:i + 49].count(1))
print(m)







answer = 19

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 14, answer, '1f0e3dad99908345f7439f8ffabdffc4'))