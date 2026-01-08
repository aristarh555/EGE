# Решение
from itertools import product

count = 0
for p in product('2468', '1357', '2468', '1357', '2468', '1357','2468', '1357','2468', '1357', '2468'):
    if p.count('1') < 4 and p.count('2') < 4 and p.count('3') < 4 and p.count('4') < 4 and p.count('5') < 4 and p.count('6') < 4 and p.count('7') < 4 and p.count('8') < 4:
        count += 1
# * 2, потому что можно начинать с гласной, а можно и с согласной
print(count * 2)






answer = 6681600

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 17, answer, 'd67d496249f30f93dd6a7a6d84701d60'))