class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = []
        for i in range(m):
            row = []
            for j in range(n):
                if i == 0 or j == 0:
                    row.append(1)
                else:
                    row.append(0)
            mat.append(row)

        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i-1][j] + mat[i][j-1]

        return mat[-1][-1]