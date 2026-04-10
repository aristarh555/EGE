# Решение
f = open('-Задание 1702.txt', 'r')
a = f.readlines()
f.close()
for i in range(len(a)):
    a[i] = int(a[i])
count = 0
max_r = 0
for x in range(len(a)):
    for y in range(x+1, len(a)):
        if abs(a[x] - a[y]) % 60 == 0 and (a[x] % 15 == 0  or a[y] % 15 == 0) and x != y:
            count += 1
            if abs(a[x] - a[y]) > max_r:
                max_r = abs(a[x] - a[y])
print(count, max_r)











answer1 = 63517
answer2 = 9960

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1702, f'{answer1} {answer2}', '1f1b321d4ee0f8a0a2de5ccf29035748'))