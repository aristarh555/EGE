for a in range(200):
    for x in range(200):
        if not(((x & 57 > 0) or (x & 99 > 0))<= (x & a > 0)):
            break
    else:
        print(a)
        break
        