# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        def in_bound(r,c):
            return 0<=r<m and 0<=c<n
        m, n  = len(dungeon), len(dungeon[0])
        dirs = [(0,1),(1,0)]
        dp = {}
        def dfs(r, c):
            if (r,c) == (m-1,n-1):
                return dungeon[r][c] if dungeon[r][c] < 0 else 0 
            if (r,c) in dp:
                return dp[(r,c)]
            max_health = float('-inf')
            for rc, cc in dirs:
                nr, nc = rc + r, cc + c
                if in_bound(nr,nc):
                    max_health = max(dfs(nr,nc), max_health)    

            dp[(r,c)] = min(0,max_health + dungeon[r][c])
            return dp[(r,c)]
        return -dfs(0,0) + 1