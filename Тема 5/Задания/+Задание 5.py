# Решение
for n in range(1, 100000):
    bn = bin(n)[2:]
    bn = bn.replace('0', 'x')
    bn = bn.replace('1', '0')
    bn = bn.replace('x', '1')
    r = int(bn, 2)
    res = n - r
    if res == 999:
        print(n)
        break







answer = 1011

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 5, answer, '7f975a56c761db6506eca0b37ce6ec87'))