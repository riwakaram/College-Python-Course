def transpose(lst):
    return [[row[i] for row in lst] for i in range(len(lst[0]))]


def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return " "


def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return " "


def checkWin(board):
    for newBoard in [board, transpose(board)]:
        result = checkRows(newBoard)
        if result != " ":
            return result
    return checkDiagonals(board)


a = [['O', 'O', 'X'],
     ['X', 'O', 'X'],
     ['O', 'X', 'X']]
print(checkWin(a))
