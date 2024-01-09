class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for r in range(m-2):

            for c in range(n-2):

                top = sum(grid[r][c:c+3])
                mid = grid[r+1][c+1]
                bot = sum(grid[r+2][c:c+3])

                if top + mid + bot > ans:
                    ans = top + mid + bot 
        return ans