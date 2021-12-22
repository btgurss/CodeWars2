def valid_solution(board):
    n = 0
    while n < 9:
        rowChecker = []
        columnChecker = []
        for num in (board[n]):
            if num == 0:
                return False
            elif num not in rowChecker:
                rowChecker.append(num)
            else:
                return False
        n += 1
        h = 0
        while h < 9:
            temp = board[h][n-1]
            if temp not in columnChecker:
                columnChecker.append(temp)
            else:
                return False
            h += 1
    count = 0
    while count < 9:
        section1 = []
        section2 = []
        section3 = []
        for i in range(count, count + 3):
            for j in range(0, 3):        
                if board[i][j] not in section1:
                    section1.append(board[i][j])
                else:
                    return False
            for m in range(3, 6):
                if board[i][m] not in section2:
                    section2.append(board[i][m])
                else:
                    return False
            for n in range(6, 9):
                if board[i][n] not in section3:
                    section3.append(board[i][n])
                else:
                    return False
            print(section1)
            print(section2)
            print(section3)
        count = count + 3
    return True   




test = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]]
print(valid_solution(test))