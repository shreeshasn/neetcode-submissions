class Solution:
    def climbStairs(self, n: int) -> int:
        # def fibo(n):
        #     a,b = 0,1
        #     for _ in range(1,n+1):
        #         a,b=b,a+b
        #     return b
        # return fibo(n)

        d = {}
        def climb(n):
            if n == 1 or n == 2:
                return n
            if n-1 not in d:
                d[n-1] = climb(n-1)
            if n-2 not in d:
                d[n-2] = climb(n-2)
            return d[n-1]+d[n-2]
        return climb(n)