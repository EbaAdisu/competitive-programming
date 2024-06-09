# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def isBound(r,c):
            return 0 <= r < m and 0 <= c < n
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(row,col):
            visited.add((row,col))
            area = 1
            for row_change, col_change in directions:
                new_row = row_change + row
                new_col = col_change + col
                # print(row,col, ':>', row_change, col_change,(new_row, new_col))
                if isBound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col]==1:
                    area += dfs(new_row, new_col)
            return area
        visited = set()
        answer = 0
        for row in range(m):
            for col in range(n):
                if (row,col) not in visited and grid[row][col]:
                    answer = max(dfs(row,col),answer)
        return answer