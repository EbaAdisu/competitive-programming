# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
            
        m, n = len(t), len(s)
        def inbound(r,c):
            if 0<=r <m and  0<=c<n:
                return dp[r][c]
            return 0
        dp = [[0] * n for i in range(m)]
        for r in range(m):
            for c in range(n):
                if s[c] == t[r]:
                    dp[r][c] = 1 + inbound(r-1, c-1)
                else:
                    dp[r][c] = max(inbound(r-1,c), inbound(r,c-1))
        return dp[-1][-1] == n


        dp = {}
        def dfs(i, j):
            if j >= len(s) :
                return True
            if i >= len(t):
                return False
            if (i,j ) in dp:
                return dp[(i,j)]
            pick = False
            no_pick = dfs(i+1,j)
            if t[i] == s[j]:
                pick = dfs(i+1,j+1)
            dp[(i,j)] = pick or no_pick
            return dp[(i,j)]
        return dfs(0,0)

        