# Решение
def game(heap, moves, to):
    if heap > 19:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap-5, moves+1, to)]
    if heap % 2 == 0:
        h.append(game(heap//2, moves+1, to))
    if heap % 3 == 0:
        h.append(game(heap//3, moves+1, to))
    if heap % 2 != 0 and heap % 3 != 0:
        h.append(game(heap+1, moves+1, to))
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)
print(min(s for s in range(19, 10000) if not game(s, 0, 1) and game(s, 0, 2)))





answer = 20

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(19, 1903, answer, '8e296a067a37563370ded05f5a3bf3ec'))