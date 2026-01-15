for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (x or (not(y))) <= (w == z) == 0:
                    print(x, y, z, w)
print('//////')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (x or (not(y))) == (w <= z) == 0:
                    print(x, y, z, w)







answer = 'zxyw'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 11, answer, '7379de4777f5748aa568b8d0bf8c3795'))