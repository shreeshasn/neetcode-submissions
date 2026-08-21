# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # nums = []
        # for i in candidates:
        #     if i <= target:
        #         nums.append(i)

        # if not nums:
        #     return []

        # nums = sorted(nums)
        # d = Counter(nums)
        # res = []

        # def dfs(i, cur, total, cur_d):
        #     if i >= len(nums) or total > target or cur_d.get(nums[i],0) > d[nums[i]]:
        #         return
        #     if total == target:
        #         res.append(cur[:])
        #         return
            
        #     cur.append(nums[i])
        #     cur_d[nums[i]] = cur_d.get(nums[i],0)+1
            
        #     dfs(i, cur, total + nums[i], cur_d)
            
        #     cur.pop()
        #     cur_d[nums[i]] = cur_d.get(nums[i],1)-1
            
        #     dfs(i + 1, cur, total, cur_d)

        # dfs(0, [], 0, {})

        # ans = []
        # for i in res:
        #     if i not in ans:
        #         ans.append(i)
        # return ans

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return res