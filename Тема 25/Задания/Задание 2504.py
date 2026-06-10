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





# Ответ в виде списка чисел []
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2504, answer, '4f6cb100db828c27d436322ae3bffeef'))