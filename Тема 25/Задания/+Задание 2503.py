# Решение

def get_divs(n):
    divs = set()
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.add(div)
            divs.add(n // div)
    return len(divs) + 2
c = 0
l = []
for i in range(999999999, 100000001, -1):
        if (i-get_divs(i)) % 23 == 0:
            c += 1
            l.append(i)
            print(i)
        if c == 5:
            break





# Ответ в виде списка чисел []
answer = [999999690, 999999731, 999999740, 999999789, 999999961] 

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2503, answer, 'c867bc32545e94925e8d2198ad7333d9'))