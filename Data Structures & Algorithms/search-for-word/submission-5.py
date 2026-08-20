class Solution:
    def exist(self, board, word):
        row_n, col_n, word_n= len(board) , len(board[0]), len(word)

        def check(row, col, ind):
            if 0<=row and row<row_n and 0<=col and col<col_n:
                if ind == word_n-1:
                    if board[row][col] == word[ind]:
                        return True
                    else:
                        return False
                else: 
                    if board[row][col] == word[ind]:
                        
                        temp = board[row][col]
                        board[row][col] = "-1"
                        
                        below = check(row+1,col,ind+1)
                        above = check(row-1,col,ind+1)
                        right = check(row,col+1,ind+1)
                        left = check(row,col-1,ind+1)
                        
                        if below or above or left or right:
                            return True
                        
                        board[row][col] = temp
                    else:
                        return False
            else:
                return False

        for r in range(row_n):
            for c in range(col_n):
                if board[r][c] == word[0] and check(r,c,0):
                    return True
        
        return False