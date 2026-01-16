lst = [0] * 10000

for n in range(1, 1000):
    b = bin(n)[2:]
    b += bin(n % 4)[2:]
    r = int(b, 2)
    lst[r] = 1

m = 0
for i in range(len(lst) - 65):
    m = max(m, lst[i:i + 65].count(1))
print(m)