def valid_solution(board):
    checker = []
    n = 0
    while n < 9:
        rowChecker = []
        columnChecker = []
        for num in (board[n]):
            if num not in rowChecker:
                rowChecker.append(num)
                n += 1
            else:
                return False
        h = 0
        while h < 9:
            for num2 in board[h][n]:
                if num2 not in columnChecker:
                    columnChecker.append(num2)
                    h += 1
                else:
                    return False
    print(rowChecker)
    print(columnChecker)   




test = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]]
valid_solution(test)