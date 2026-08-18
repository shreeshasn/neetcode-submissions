class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # res = []
        # nums = sorted(nums)
        # seen = set()
        # def checkComb(cur):
        #     key = tuple(sorted(cur))
        #     if key not in seen:
        #         seen.add(key)
        #         res.append(cur)
                
        # def comb(nums, cur, cursum):
        #     if cursum > target:
        #         return

        #     for i in nums:
        #         if i+cursum == target:
        #             cur = cur + [i]
        #             checkComb(cur)

        #         elif i+cursum < target:
        #             comb(nums, cur+[i], i+cursum)
            
        # for i in nums:
        #     if i == target:
        #         res.append([target])
        #         break
        #     elif i < target:
        #         comb(nums, [i], i)

        # return res

        # # ans = []
        # # for i in res:
        # #     if sum(i) == target:
        # #         cur = sorted(i)
        # #         if cur not in ans:
        # #             ans.append(cur)
        # # return ans

        
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res





















