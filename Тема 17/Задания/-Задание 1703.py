# Решение
f = open('-Задание 1703.txt', 'r')
a = f.readlines()
f.close()
min_x = 100000
for y in range(len(a)):
    a[y] = int(a[y])
for x in range(len(a)):
    if (abs(a[x]) % 100) // 10 == abs(a[x]) % 10 and a[x]< min_x:
        min_x = a[x]
c = 0
maxx = -100000
for i in range(len(a)-1):
    flag = 0
    if (abs(a[i]) % 10 == ((abs(a[i+1])%100) // 10)) != (abs(a[i+1]) % 10 == ((abs(a[i]) % 100) // 10)):
        flag += 1
    if (a[i] % 13 == 0) != (a[i+1] % 13 == 0):
        flag += 1

    if (a[i]**2 + a[i+1]**2) <= min_x**2:
        flag += 1
    if flag == 3:
        c += 1
        if (a[i]**2 + a[i+1]**2) > maxx:
            maxx = a[i]**2 + a[i+1]**2
print(c, maxx)








answer1 = 113
answer2 = 96944186

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1703, f'{answer1} {answer2}', '1b1a3f384b8b6bddea7c6e63fad46024'))