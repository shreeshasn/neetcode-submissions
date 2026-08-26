class Solution:
    def letterCombinations(self, s):
        res = []
        n = len(s)
        
        if not s:
            return res
        
        d = {
            2 : "abc", 3 : "def", 4 : "ghi", 5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"
        }
        l = []

        for i in s:
            l.append(d[int(i)])

        def comb(cur, li, m):
            if m == n:
                res.append(cur[:])
                return
            for j in l[li]:
                comb(cur+j, li+1, m+1)
            
        comb("", 0, 0)
        return res