# Решение
f = open('Задание 1706.txt', 'r')
a = list(map(int ,f.readlines()))
f.close()
max_33 = -100001
for i in a:
    if int(i) > max_33 and int(i) % 100 == 33:
        max_33 = int(i)
d2 = range(10, 99)
c = 0
maxx = -300003
for j in range(len(a)-2):
    flag = 0
    if int(abs(a[j]) in d2) + int(abs(a[j+1]) in d2) + int(abs(a[j+2]) in d2) >= 2:
        flag += 1
    if (int(a[j] + a[j+1] + a[j+2]))**2 <= max_33:
        flag += 1
    if flag == 2:
        c += 1
        if a[j] + a[j+1] + a[j+2] > maxx:
            maxx = a[j] + a[j+1] + a[j+2]
print(c, maxx)







answer1 = 28
answer2 = 237

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1706, f'{answer1} {answer2}', 'ca4d656e61cf4b93ff4db984ee35e5dc'))