# Решение
def to_3(n):
    if n == 0:
        return '0'
    ternary = ''
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
    return ternary

for n in range(1, 10000000):
    tn = to_3(n)
    if n % 3 == 0:
        tn = tn + tn[-2:]
    elif n % 3 != 0:
        tn = str(tn) + str(to_3(5*(n%3)))
    r = int(tn, 3)
    if r <= 173:
        print(r)
    break






answer = 162

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 55, answer, '82aa4b0af34c2313a562076992e50aa3'))