# Решение
f = open('Задание 1705.txt', 'r')
a = f.readlines()
f.close()
maxx = 0
for j in a:
    if int(j) > maxx and int(j) % 100 == 17:
        maxx = int(j)
c = 0
maxxx = 0
for i in range(len(a)-3):
    flag = 0
    if (len(a[i]) == 3 and len(a[i+1]) == 3) != (len(a[i]) == 3 and len(a[i+2]) == 3) != (len(a[i+1]) == 3 and len(a[i+2]) == 3):
        flag += 1
    if int(a[i]) % 5 == 0 or int(a[i+1]) % 5 == 0 or int(a[i+2]) % 5 == 0:
        flag += 1
    if int(a[i]) + int(a[i+1]) + int(a[i+2]) > maxx:
        flag += 1
    if flag == 3:
        c += 1
        if int(a[i]) + int(a[i+1]) + int(a[i+2]) > maxxx:
            maxxx = int(a[i]) + int(a[i+1]) + int(a[i+2])
print(c, maxxx)










answer1 = 2
answer2 = 100108

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1705, f'{answer1} {answer2}', 'e7eedde909e984c854776fabd948a26f'))