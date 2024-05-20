# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def ind(r,c):
            if 0 <= r < m and 0 <= c < n and not grid[r][c]:
                return dp[r][c]
            return 0
        grid = obstacleGrid
        if grid[0][0]: 
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        for r in  range(m):
            for c in range(n):
                if not grid[r][c]:
                    dp[r][c] += (ind(r-1,c) + ind(r,c-1))
        return dp[-1][-1]


