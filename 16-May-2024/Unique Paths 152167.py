# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def inbound(r,c):
            return 0<=r<m and 0<=c<n
        dp = [[0]* n for i in range(m)]
        dp[0][0] = 1
        for r in range(m):
            for c in range(n):
                if c > 0:
                    dp[r][c]+= dp[r][c-1]
                if r > 0:
                    dp[r][c]+= dp[r-1][c]
        return dp[-1][-1]
