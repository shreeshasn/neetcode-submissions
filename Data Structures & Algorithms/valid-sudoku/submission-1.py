# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         def rowcol(board):
#             for row in board:
#                 seen = []
#                 for i in row:
#                     if i != ".":
#                         if i in seen:
#                             return False
#                         else:
#                             seen.append(i)
#             return True
        
#         def sub(board,row,col):
#             curr = []
#             for i in range(row, row+3):
#                 for j in range(col, col+3):
#                     if board[i][j] != ".":
#                         curr.append(board[i][j])
#             for i in curr:
#                 j = i
#                 curr.remove(i)
#                 if j in curr:
#                     return False
#             return True

#         if rowcol(board):
#             if sub(board,0,0) and sub(board,0,3) and sub(board,0,6) and sub(board,3,0) and sub(board,3,3) and sub(board,3,6) and sub(board,6,0) and sub(board,6,3) and sub(board,6,6):
#                 for i in range(4):
#                     for j in range(4):
#                         temp = board[i][j]
#                         board[i][j] = board[j][i]
#                         board[j][i] = temp
#                 if rowcol(board):
#                     return True
#         return False

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True