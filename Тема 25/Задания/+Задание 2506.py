# Решение
'''
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
def find_m(n):
    maxx = -1
    minn = n+1
    for i in get_divs(n):
        if prost(i) and i > maxx:
            maxx = i
        if prost(i) and i < minn:
            minn = i
    if maxx == -1 and minn == n+1:
        return 0
    else:
        return maxx + minn
for i in range(7800000, 10000000000):
    prost_l = []
    for j in get_divs(i):
        if prost(j):
            prost_l.append(j)
    if find_m(i) % 100 == 63 and find_m(i) % len(prost_l) == 0:
        print(i, find_m(i))
'''






# Ответ в виде списка чисел []
# 1й столбец
answer1 = [7800610, 7801042, 7801312, 7801916, 7802032]
# 2й столбец
answer2 = [780063, 8463, 1863, 8163, 69663]

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(25, 2506, answer1 + answer2, 'e6da587657bbbab0d1ca022034492d03'))