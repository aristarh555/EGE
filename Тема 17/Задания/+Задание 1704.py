# Решение
f = open('Задание 1704.txt', 'r')
a = f.readlines()
f.close()
minn = 100001
for j in range(len(a)):
    a[j] = int(a[j])
for i in a:
    if i < minn and i > 99 and i < 1000 and i % 10 == 5:
        minn = i
min_x = 1000000000
c = 0
for x in range(len(a)-1):
    flag = 0
    if ((a[x] > 99 and a[x] < 1000) and (a[x+1] > 999 or a[x+1] < 100)) or ((a[x+1] > 99 and a[x+1] < 1000) and (a[x] > 999 or a[x] < 100)) and (not(((a[x] > 99 and a[x] < 1000) and (a[x+1] < 1000 and a[x+1] > 99)))) and not(((a[x] > 999 and a[x] < 100) and (a[x+1] < 100 and a[x+1] > 999))):
        flag += 1
    if (a[x] + a[x+1]) % minn == 0:
        flag += 1
    if flag == 2:
        c += 1
        if a[x] + a[x+1] < min_x:
            min_x = a[x] + a[x+1]
print(c, min_x)











answer1 = 2
answer2 = 33120

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1704, f'{answer1} {answer2}', 'f3c45887478efcf9fcf722ab4708387d'))