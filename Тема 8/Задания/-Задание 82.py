# Решение
from itertools import product

i = 1
for line in product('АКОРСТ', repeat=5):
    line = "".join(line)
    if line[0] not in 'АСТ' and line.count('О') == 2 and i % 2 != 0:
        print(i)
    i += 1







answer = 5163

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 82, answer, '7ffb4e0ece07869880d51662a2234143'))