class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def sub(nums, temp, i):
            if i == len(nums):
                res.append(temp[:])
                return
            sub(nums,temp,i+1)
            sub(nums, temp + [nums[i]] , i+1)

        sub(nums, [], 0)
        print(res)
        return res