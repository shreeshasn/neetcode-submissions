class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)

        return sorted(nums)[0]

        # l = 0
        # r = len(nums)-1
        # while l<r:
        #     mid = (l+r)//2
        #     print(l,mid,r)
        #     if nums[mid] < nums[l] and nums[mid] < nums[r]:
        #         return mid
        #     elif nums[mid] > nums[r]:
        #         r = mid-1
        # return r