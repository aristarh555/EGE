# Решение
def game(heap, moves, to):
    if heap <= 20007:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap-2, moves + 1, to),
         game(heap-7, moves + 1, to),
         game(heap//3, moves + 1, to),]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)
print([s for s in range(20008, 100000) if not game(s, 0, 1) and game(s, 0, 3)])
print(min(s for s in range(16, 100000) if not game(s, 0, 2) and game(s, 0, 4)))






answer1 = 60026
answer2 = 60027

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(20, 2004, f'{answer1} {answer2}', '2d18a60f2dac95ca869006f0695ce088'))