input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

boards = []

for boardString in input.split("\n\n"):
    if boardString == "":
        continue
    board = []
    for line in boardString.split("\n"):
        if line == "":
            continue
        board.append(list(line))
    boards.append(board)


for board in boards:
    for line in board:
        print(line)
    print()

for board in boards:
    # we want to trial each column and move out for the given width to check rotation
    for c in len(board[0]):
        w = min(c, len(board[0]) - c)
        for reflection_c in range(w):
            for r in range(len(board)):
                if board[r][reflection_c] != board[r][c]:
                    break
