from itertools import product

count = 0
for p in product('РСМХ', 'ОА', 'РСМХ', 'ОА','РСМХ', 'ОА', 'РСМХ', 'ОА'):
    if p.count('О') == 2 and p.count('А') == 2 and p.count('Р') == 1 and p.count('С') == 1 and p.count('М') == 1 and p.count('Х') == 1:
        count += 1
# * 2, потому что можно начинать с гласной, а можно и с согласной
print(count * 2)
# Решение







answer = 288

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 81, answer, '48aedb8880cab8c45637abc7493ecddd'))