from itertools import combinations


p = [1, 2, 3, 4, 5, 6]
q = [3, 6, 9, 12]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for r in range(len(numbers) + 1):
    for a in combinations(numbers, r):
        if all(not(x not in a and x in q) or x not in p for x in range(1, 13)):
            print(a)



