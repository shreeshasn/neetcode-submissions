class Solution:
    def generateParenthesis(self, n):
        if n < 1:
            return []
        if n == 1:
            return ["()"]

        def isValid(s):
            if not s:
                return True
            if s[0] == ")":
                return False
            st = []
            for i in s:
                if i == "(":
                    st.append(i)
                else:
                    if not st or st.pop() != "(":
                        return False
            if not st:
                return True
            return False

        res = []
        def backtrack(cur):
            if len(cur) == 2*n and isValid(cur):
                res.append(cur[::])
                return
            if len(cur) > 2*n:
                return
            l = cur+"("
            backtrack(l)
            r = cur+")"
            backtrack(r)

        backtrack("")
        
        return res