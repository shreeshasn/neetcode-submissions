import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = nums[:i]+nums[i+1:]
            res.append(math.prod(temp))
        return res