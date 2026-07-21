class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums) or len(nums) == 1:
            return [max(nums)]
        if k == 1:
            return nums
        res = [max(nums[:k])]
        for i in range(1, len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res