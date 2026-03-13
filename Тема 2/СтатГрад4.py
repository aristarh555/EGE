'''from itertools import product

print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if not(y and (not(w) or z == x)):
        print(x, y, z, w)
'''

from itertools import product, permutations


def f1(x, y, z, w):
    return y and (not(w) or z == x)


for a0, a1, a2, a3, a4 in product((0, 1), repeat=5):
    s = [(a0, a1, 0, 0, 1),
         (a2, 1, 1, 1, 0),
         (0, a3, a4, 0, 1)]
    if len(set(s)) == len(s):
        for x, y, z, w in permutations((0, 1, 2, 3)):
            if all([f1(i[x], i[y], i[z], i[w]) == i[-1] for i in s]):
                print(f'x = {x + 1}; y = {y + 1}; z = {z + 1}; w = {w + 1}')
                break
