class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)

        p2, p1 = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            temp = max(p1, p2+nums[i])
            p2 = p1
            p1 = temp

        return p1