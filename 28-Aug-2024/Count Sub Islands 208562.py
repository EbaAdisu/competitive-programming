# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n = len(grid1), len(grid1[0])
        def inbound(r,c):
            return 0<=r<m and 0<=c<n and grid2[r][c] == 1

        def dfs(r,c):
            visited.add((r,c))
            ans = grid1[r][c]
            for rc,cc in dirs:
                nr,nc = rc + r, cc + c
                if inbound(nr,nc) and (nr,nc) not in visited:
                    ans = min(ans, dfs(nr,nc))
            return ans
        
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        total = 0
        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1 and (r,c) not in visited:
                    total += dfs(r,c)
                    # print(r,c,total )
        return total

            