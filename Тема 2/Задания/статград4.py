for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(y and (not(w) or (z == x))):
                    print(x, y, z, w)