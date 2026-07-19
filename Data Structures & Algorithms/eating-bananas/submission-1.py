class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # s = sorted(piles)
        # speed = 1
        # while speed <= s[-1]:
        #     cur = 0
        #     for i in s:
        #         cur += math.ceil(i/speed)
        #         if cur > h:
        #             break
        #     if cur <= h:
        #         return speed
        #     speed += 1
        # return -1

        s = sorted(piles)
        l = 1
        r = s[-1]
        res = s[-1] # because max pile amount is the max allowed K
        while l<=r:
            midspeed = (l+r)//2
            cur = 0
            for i in s:
                cur += math.ceil(i/midspeed)
                if cur > h:
                    break
            if cur <= h:
                res = midspeed
                r = midspeed - 1
            else:
                l = midspeed + 1
        return res
