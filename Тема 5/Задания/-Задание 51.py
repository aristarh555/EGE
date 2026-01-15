# Решение
c = 0
for n in range(1, 100000000000000000000000):
    bn = bin(n)[2:]
    y = bin(int(bn, 2) % 3)[2:]
    bn = str(bn) + str(y)
    x = bin(int(bn, 2) % 5)[2:]
    r = str(bn) + str(x)
    r = int(r, 2)
    if r <= 1444444416 and r >= 1111111110:
        c += 1
    elif r > 1444444416:
        break
print(c)








answer = 694444

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 51, answer, '389499b02f30212486e408cd73a5bc50'))