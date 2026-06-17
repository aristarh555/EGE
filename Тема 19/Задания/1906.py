def game(heap, moves, to):
    if heap <= 26005:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap-2, moves + 1, to), game(heap-7, moves + 1, to), game(heap//3, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)
print(max(s for s in range(26005, 100000) if not game(s, 0, 1) and game(s, 0, 2)))
