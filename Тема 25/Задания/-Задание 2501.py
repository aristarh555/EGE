# Решение
from fnmatch import fnmatch

for i in range(0, 10 ** 10, 2026):
    if fnmatch(str(i), '5?34?71*2'):
        print(i)





# Ответ в виде списка чисел []
answer = [553497122, 5134171692, 5134971962, 5234671422, 5434171642, 5434971912, 5534671372, 5734171592, 5734971862, 5834671322]

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2501, answer, 'ac788180ab5a2f5b1ff54976b883276a'))