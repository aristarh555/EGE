# Решение
def game(heap, moves, to):
    if heap >= 313:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap+2, moves + 1, to),
         game(heap+3, moves + 1, to),
         game(heap*2, moves + 1, to),]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)
print(max(s for s in range(1, 313) if not game(s, 0, 1) and game(s, 0, 3)), min(s for s in range(1, 313) if not game(s, 0, 1) and game(s, 0, 3)))






answer1 = 78
answer2 = 154

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(20, 2001, f'{answer1} {answer2}', '7f19aee529865f43adbed8aeffe7ac33'))