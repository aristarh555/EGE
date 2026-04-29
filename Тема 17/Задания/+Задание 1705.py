# Решение
f = open('-Задание 1705.txt', 'r')
a = list(map(int, f.readlines()))
f.close()
maxx = 0
for j in a:
    if j > maxx and j % 100 == 17:
        maxx = j
c = 0
maxxx = 0
for i in range(len(a) - 3):
    flag = 0
    if (int(len(str(a[i])) == 4) + int(len(str(a[i + 1])) == 4) + int(len(str(a[i + 2])) == 4)) == 2:
        flag += 1
    if (a[i] % 5 == 0) or (a[i + 1] % 5 == 0) or (a[i + 2] % 5 == 0):
        flag += 1
    if (a[i] + a[i + 1] + a[i + 2]) > maxx:
        flag += 1
    if flag == 3:
        c += 1
        if (a[i] + a[i + 1] + a[i + 2]) > maxxx:
            maxxx = a[i] + a[i + 1] + a[i + 2]
print(c, maxxx)

answer1 = 21
answer2 = 114132

#

from tests.conftest import result_register

if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1705, f'{answer1} {answer2}', 'e7eedde909e984c854776fabd948a26f'))
