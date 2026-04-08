# Решение
'''
def prost(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def find_s(n):
    summ = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 and prost(i):
            summ += i
        if prost(n//i) and n % (n//i) == 0:
            summ += n//i

    return summ
for i in range(1325000, 0, -1):
    s = find_s(i)
    if s != 0 and s <= 30000 and s % 5 == 0:
        print(i)
'''






# Ответ в виде списка чисел []
answer = [1324994, 1324992, 1324991, 1324986, 1324980]

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2502, answer, 'a4962eab53c004fe8f3ffaca3207d0fa'))