# Решение
def game(heap, moves, to):
    if heap >= 313:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap + 2, moves + 1, to),
         game(heap + 3, moves + 1, to),
         game(heap * 2, moves + 1, to)]
    # any(<массив лог. значений>) - функция, возвращает true,
    # если хотя бы одно значение в массиве истинно
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print('19: ', [s for s in range(1, 313) if not game(s, 0, 1) and game(s, 0, 2)])

answer = 311

#

from tests.conftest import result_register

if answer is not Ellipsis:
    print(result_register(19, 1901, answer, '9dfcd5e558dfa04aaf37f137a1d9d3e5'))
