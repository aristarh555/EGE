def game(heap, moves, to):
    if heap <= 15:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap-3, moves + 1, to),
         game(heap-7, moves + 1, to),
         game(heap//4, moves + 1, to),]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)
print(min(s for s in range(16, 100000) if not game(s, 0, 1) and game(s, 0, 2)))