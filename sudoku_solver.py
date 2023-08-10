import copy

import numpy as np


def is_valid_position(board, row: int, column: int, value: int):
    # checking the row
    for i in range(9):
        if board[row][i] == value:
            return False

    # checking the column
    for i in range(9):
        if board[i][column] == value:
            return False

    # checking the local box
    local_row = row - row % 3
    local_column = column - column % 3
    for r in range(local_row, local_row + 3):
        for c in range(local_column, local_column + 3):
            if board[r][c] == value:
                return False

    return True


def solve_board(board, solutions):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid_position(board, i, j, num):
                        board[i][j] = num
                        solve_board(board, solutions)
                        board[i][j] = 0
                return
    solutions.add(tuple(map(tuple, copy.deepcopy(board))))


if __name__ == "__main__":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 0, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    solutions = set()

    """
    if u want to take input from user one line at a time
    """
    # board = []
    # for i in range(9):
    #     line = list(map(int, (int(x) for x in list(input()))))
    #     board.append(line)
    # for i in range(9):
    #     print(board[i])
    # print()

    """
    if u want to take whole sudoku input in one line 
    """
    # board = []
    # inp = input("Enter whole board in oneline without spaces\n")
    # x = 0
    # for i in range(9):
    #     line = []
    #     for j in range(9):
    #         line.append(int(inp[x]))
    #         x += 1
    #     board.append(line)

    solve_board(board, solutions)
    s = 1
    for solution in solutions:
        print(f"Solution {s} : ")
        s += 1
        print(np.matrix(solution))
        x = input("\nWant another solution? then type 'Y' or 'y'\n")
        if x not in ('y', 'Y'):
            print("Process ended")
            break
    else:
        print(f"this Sudoku has Only {s - 1} possible solutions")
