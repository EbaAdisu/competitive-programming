# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0]*(n+1)
        ans = n
        for i in range(2,n+1):
            for j in range(i-1,0,-1):
                if i%j == 0:
                    dp[i] = dp[j] + i//j
                    break
        # print(dp)
        return dp[-1]