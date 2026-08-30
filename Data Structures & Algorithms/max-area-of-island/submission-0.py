class Solution:
    def maxAreaOfIsland(self, mat):
        self.count = 0
        r,c = len(mat), len(mat[0])

        def dfs(i,j):
            if i >= 0 and i < r and j >= 0 and j < c and mat[i][j] == 1:
                    mat[i][j] = 0
                    self.count += 1
                    dfs(i+1,j)
                    dfs(i-1,j)
                    dfs(i,j-1)
                    dfs(i,j+1)
            else:
                return
        
        res = 0
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    self.count = 0
                    dfs(i,j)
                    res = max(self.count, res)
        return res