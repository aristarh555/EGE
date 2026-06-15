# Решение
f = open('Задание 1708.txt', 'r')
a = f.readlines()
f.close()
for j in range(len(a)):
    a[j] = int(a[j])
maxx = -1000001
for d in range(len(a)):
    if a[d] > maxx and a[d] % 100 == 15:
        maxx = a[d]
r = range(1000, 9999)
c = 0
minn = 3000003
for i in range(len(a)-2):
    flag = 0
    if (a[i] in r and a[i+1] not in r and a[i+2] not in r) or (a[i] not in r and a[i+1] in r and a[i+2] not in r) or (a[i] not in r and a[i+1] not in r and a[i+2] in r):
        flag += 1
    if a[i] + a[i+1] + a[i+2] < maxx:
        flag += 1
    if flag == 2:
        c += 1
        if a[i] + a[i+1] + a[i+2] < minn:
            minn = a[i] + a[i+1] + a[i+2]
print(c, minn)






answer1 = 2453
answer2 = -176846

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1708, f'{answer1} {answer2}', '00c6fe526fd35b34ccc48ff4693db50a'))