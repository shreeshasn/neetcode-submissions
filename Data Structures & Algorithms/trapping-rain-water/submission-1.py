class Solution:
    def trap(self, h: List[int]) -> int:
        # O(N) Brute-Force
        # res = 0
        # for i in range(1, len(h)-1):
        #     maxleft = max(h[0:i])
        #     maxright = max(h[i+1:])
        #     minval = min(maxleft, maxright) - h[i]
        #     if minval > 0:
        #         res = res + minval
        # return res
        
        res = 0

        maxl = [0]
        maxleft = 0
        for i in range(1, len(h)):
            maxleft = max(maxleft , h[i-1])
            maxl.append(maxleft)
        print(maxl)

        maxr = [0]*len(h)
        maxright = h[-1]
        for j in range(len(h)-2 , -1, -1):
            maxright = max(maxright , h[j+1])
            maxr[j]=maxright
        print(maxr)

        for k in range(len(h)):
            minval = min(maxl[k] , maxr[k]) - h[k]
            if minval > 0:
                res+=minval
                
        return res