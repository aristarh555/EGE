for a in range(100):
    if all((x + 2*y > a) or (x > 13) or (y<44) for x in range(100) for y in range(100)):
        print(a)
