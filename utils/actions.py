#Valid moves
def actions(maze, state):
    row, column = state
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = []

    for changeRow, changeColumn in moves:
        newRow, newColumn = row + changeRow, column + changeColumn

        if 0 <= newRow < 15 and 0 <= newColumn < 15 and maze[newRow][newColumn] != "#":
            result.append((newRow, newColumn))

    return result