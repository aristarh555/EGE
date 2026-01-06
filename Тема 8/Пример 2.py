from itertools import product

count = 0
for p in product('ЕЯ', 'ПТ', 'ЕЯ', 'ПТ', 'ЕЯ', 'ПТ'):
    count += 1
# * 2, потому что можно начинать с гласной, а можно и с согласной
print(count * 2)


# Короткая версия
print(len(list(product('ЕЯ', 'ПТ', 'ЕЯ', 'ПТ', 'ЕЯ', 'ПТ'))) * 2)