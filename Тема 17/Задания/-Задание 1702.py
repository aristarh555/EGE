# Решение
f = open('Задание 1702.txt', 'r')
a = f.readlines()
f.close()
for i in range(len(a)):
    a[i] = int(a[i])
count = 0
max_r = 0
for z in range(len(a)-1):
    if abs(a[z] - a[z + 1]) % 60 == 0 and (a[z] % 15 == 0  or a[z+1] % 15 == 0):
        count += 1
        if abs(a[z] - a[z + 1]) > max_r:
            max_r = abs(a[z] - a[z + 1])
print(count, max_r)











answer1 = 9
answer2 = 5340

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1702, f'{answer1} {answer2}', '1f1b321d4ee0f8a0a2de5ccf29035748'))