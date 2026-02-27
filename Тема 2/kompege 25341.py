from itertools import product
print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if not((w == z) or not(y <= w) or not(x)):
        print(x, y, z, w)