class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve_n_queens(n):
            res = []
            cols, diag1, diag2 = set(), set(), set()
            board = []
            def backtrack(row):
                if row == n:
                    res.append(board[:])
                    return
                for col in range(n):
                    if col in cols or (row - col) in diag1 or (row + col) in diag2:
                        continue
                    cols.add(col); diag1.add(row - col); diag2.add(row + col)
                    board.append(col)
                    backtrack(row + 1)
                    board.pop()
                    cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)
            backtrack(0)
            return res

        mat = solve_n_queens(n)

        ans = []
        for comb in mat:
            temp = []
            for i in range(n):
                t = []
                for j in range(n):
                    t.append(".")
                temp.append(t)
            i = 0
            for ind in comb:
                temp[i][ind] = "Q"
                i = i + 1
            ans.append(temp)
        
        res = []
        for c in ans:
            x = []
            for r in c:
                x.append(''.join(r))
            res.append(x)
        return res