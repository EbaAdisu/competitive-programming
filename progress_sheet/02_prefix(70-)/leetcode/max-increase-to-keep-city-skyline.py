class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid),len(grid[0])
        row = [max(row) for row in grid]
        col = []
        for c in range(n):
            colMax = 0
            for r in range(len(grid)):
                if grid[r][c] > colMax:
                    colMax = grid[r][c]
            col += [colMax]
        total = 0
        for r in range(m):
            for c in range(n):
                minMax = min(col[c],row[r])
                total += minMax - grid[r][c]

        return total

