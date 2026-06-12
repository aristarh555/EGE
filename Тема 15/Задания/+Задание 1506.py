# Решение
'''
p = range(167242, 514210)
q = range(403149, 718530)
r = range(522897, 816282)
min_len = 1000000
for begin in range(800000):
    for end in range(800000):
        a = range(begin, end)
        if all((x in q) <= (((x in p) or (x in r)) <= (x in a)) for x in range(800000)):
            min_len = min(min_len, end - begin)
print(min_len)
'''





answer = 315382

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1506, answer, 'e0ee0001e619cc4b3b2113d235f9416f'))