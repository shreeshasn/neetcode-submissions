class Solution:
    def maxArea(self, h: List[int]) -> int:
        # res = 0
        # for i in range(len(h)):
        #     for j in range(i+1, len(h)):
        #         res = max(res, min(h[i], h[j]) * (j-i) )
        # return res
        
        res = 0
        l,r = 0,len(h)-1
        while l < r:
            res = max( res  , min(h[l] , h[r]) * (r-l) )
            if h[l] <= h[r]:
                l = l+1
            else:
                r = r-1
        return res
