class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # d = Counter(nums)
        # for i in d:
        #     if d[i] == 1:
        #         return i

        x = 0
        for i in nums:
            x ^= i
        return x