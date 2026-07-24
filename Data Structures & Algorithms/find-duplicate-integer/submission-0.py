class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d= {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        for j in d.keys():
            if d[j] > 1:
                return j
        return -1