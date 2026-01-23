for n in range(123456790 - 8, 123456790 + 1):
    b = bin(n)[2:]
    r = n
    for _ in range(3):
        c1 = str(r).count('2') + str(r).count('4') + str(r).count('6') + str(r).count('8') + str(r).count('0')
        c2 = str(r).count('1') + str(r).count('3') + str(r).count('5') + str(r).count('7') + str(r).count('9')
        if c1 > c2:
            b += '1'
        elif c2 > c1:
            b += '0'
        else:
            if r % 2 == 0:
                b += '0'
            else:
                b += '1'
        r = int(b, 2)
    print(n, r, r // n)

# Нашли закономерность = 8
# Начало 123455
# Конец  987654321


# Первое в диапазоне: 123458
# Последнее число в диапазоне: 987654312

start = 123458
count = 1
while start <= 987654312:
    start += 8
    count += 1
print(count)

