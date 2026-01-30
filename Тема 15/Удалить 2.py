for a in range(64):
    if all((x & 30 == 0) or ((x & 57 == 0) <= (x & a != 0)) for x in range(64)):
        print(a)
        break