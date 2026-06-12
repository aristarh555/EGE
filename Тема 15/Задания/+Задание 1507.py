# Решение
p = range(17, 54)
q = range(37, 83)
min_len = 1000
for begin in range(400):
    for end in range(400):
        a = range(begin, end)
        if all((x in p) <= (((x in q) and (not(x in a))) <= (not(x in p))) for x in range(400)):
            min_len = min(min_len, end - begin)
print(min_len)





answer = 17

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1507, answer, '70efdf2ec9b086079795c442636b55fb'))