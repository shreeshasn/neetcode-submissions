class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = sorted(list(set(nums)))
        
        if len(nums) < 1:
            return 0

        print(d)

        res = 1
        streak = 1
        for i in range(1,len(d)):
            if d[i]==d[i-1]+1:
                streak = streak + 1
            else:
                res = max(streak,res)
                streak = 1

        res = max(streak , res)
        return res