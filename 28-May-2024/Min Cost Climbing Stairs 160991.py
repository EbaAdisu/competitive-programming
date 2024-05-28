# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * (N + 1)
        for i in range(N+1):
            if i > 1:
                dp[i] = min(dp[i-1] + cost[i-1],dp[i-2]  + cost[i-2])
        return dp[-1]
        
        