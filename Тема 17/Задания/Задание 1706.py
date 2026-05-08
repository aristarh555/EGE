# Решение
f = open('Задание 1706.txt', 'r')
a = f.readlines()
f.close()
for x in a:
    x = x[:2]
    x = int(x)
max_33 = -100001
for i in a:
    if int(i) > max_33 and int(i) % 100 == 33:
        max_33 = int(i)
d2 = range(10, 99)
d_2 = range(-99, -10)
c = 0
maxx = -300003
for j in range(len(a)-2):
    flag = 0
    if (a[j] in d2 or a[j] in d_2 and a[j+1] in d2 or a[j+1] in d_2) or (a[j] in d2 or a[j] in d_2 and a[j+2] in d2 or a[j+2] in d_2) or (a[j+1] in d2 or a[j+1] in d_2 and a[j+2] in d2 or a[j+2] in d_2):
        flag += 1
    if (int((a[j] + a[j+1] + a[j+2])[:2]))**2 <= max_33:
        flag += 1
    if flag == 2:
        c += 1
        if a[j] + a[j+1] + a[j+2] > maxx:
            maxx = a[j] + a[j+1] + a[j+2]
print(c, maxx)







answer1 = ...
answer2 = ...

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1706, f'{answer1} {answer2}', 'ca4d656e61cf4b93ff4db984ee35e5dc'))