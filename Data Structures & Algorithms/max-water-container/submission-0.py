class Solution:
    def maxArea(self, h: List[int]) -> int:
        res = 0
        for i in range(len(h)):
            for j in range(i+1, len(h)):
                res = max(res, min(h[i], h[j]) * (j-i) )
        return res