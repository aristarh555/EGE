for n in range(2, 1000):
    b = bin(n)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    if int(b, 2) > 77:
        print(n)
        break
