# Решение
def get_divs(n):
    divs = set()
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.add(div)
            divs.add(n // div)
    return sorted(divs)

def prost(n):
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True
def prost_divs(n):
    l = []
    for i in get_divs(n):
        if prost(i):
            l.append(i)
    return l
l = []
for i in range(4555705, 1000000000):
    if i % 10 != 3:
        x = i - (sum(prost_divs(i)) + 1 + len(prost_divs(i)))
        if x % 100 == 23:
            if i == sum(prost_divs(i)) + 1 + len(prost_divs(i)) + x:
                l.append(i)
                print(i, x, prost_divs(i))
    if len(l) == 5:
        print(l)
        break



# Ответ в виде списка чисел []
answer = [4555721, 4555745, 4555755, 4555846, 4555965]

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2504, answer, '4f6cb100db828c27d436322ae3bffeef'))