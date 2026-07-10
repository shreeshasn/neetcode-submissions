class Solution:
    def maxProfit(self, p: List[int]) -> int:
        res = 0
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                res = max(res , p[j]-p[i])
        return res