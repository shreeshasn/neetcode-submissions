class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p = [0]*len(cost)
        p[0],p[1] = cost[0],cost[1]

        for i in range(2, len(cost)):
            p[i] = min(p[i-1], p[i-2])+cost[i]
        
        return min(p[-1], p[-2])