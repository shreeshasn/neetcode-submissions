class Solution:
    def trap(self, h: List[int]) -> int:
        res = 0
        for i in range(1, len(h)-1):
            maxleft = max(h[0:i])
            maxright = max(h[i+1:])
            minval = min(maxleft, maxright) - h[i]
            if minval > 0:
                res = res + minval
        return res