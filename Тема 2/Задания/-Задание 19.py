# Решение
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                for u in range(0, 2):
                    if (((x <= y) and (z == (not(w)))) <= (u == (x or z))) == 0:
                        print(x, y, z, w, u)






answer = 'wzyxu'