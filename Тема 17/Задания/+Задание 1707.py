# Решение
f = open('Задание 1707.txt', 'r')
list = f.readlines()
f.close()
a = []
for l in list:
    l = int(l)
    a.append(l)
n4 = range(1000, 9999)
maxx = -1
minn = 1000000
for j in a:
    if j > maxx:
        maxx = j
    if j < minn:
        minn = j
c = 0
maxxx = -1
for i in range(len(a)-2):
    flag = 0
    if (a[i] in n4 and a[i+1] in n4) or (a[i] in n4 and a[i+2] in n4) or (a[i+1] in n4 and a[i+2] in n4):
        flag += 1
    if (a[i] % 10 == maxx % 10) or (a[i+1] % 10 == maxx % 10) or (a[i+2] % 10 == maxx % 10):
        flag += 1
    if (a[i] % 10 != minn % 10) and (a[i+1] % 10 != minn % 10) and (a[i+2] % 10 != minn % 10):
        flag += 1
    if flag == 3:
        c += 1
        if a[i] + a[i+1] + a[i+2] > maxxx:
            maxxx = a[i] + a[i+1] + a[i+2]
print(c, maxxx)












answer1 = 46
answer2 = 113153

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1707, f'{answer1} {answer2}', '73a43ee74b89a86c6d92c3c921aac771'))