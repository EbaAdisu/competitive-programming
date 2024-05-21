# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def pre(r,c):
            if 0<=c<len(dp[r]):
                return dp[r][c]
            return float('inf')
        dp = triangle
        n = len(dp)
        for r in range(1,n):
            for c in range(len(dp[r])):
                dp[r][c] += min(pre(r-1,c), pre(r-1,c-1))
        return min(dp[-1])
            
        