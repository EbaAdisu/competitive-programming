# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        # math
        count = 0
        screen = 1
        copy = 0
        while screen < n:
            if n % screen == 0:
                count += 1
                copy = screen
            screen += copy
            count += 1
        return count


        # dp

        # bottom up
        dp = [-1] * (n+1)
        dp[1] = 0
        for i in range(2,n+1):
            min_count = float('inf')
            for j in range(1, i//2 + 1):
                if i % j == 0:
                    min_count = dp[j] + i//j
            dp[i] = min_count
        # print(dp)
        return dp[-1]
        
        # top down
        @cache
        def dfs(screen, copy):
            if screen == n:
                return 0
            elif screen > n:
                return float('inf')
            min_move = float('inf')
            # copy
            if copy < screen:
                min_move = min(min_move, dfs(screen, screen))
            # paste
            if copy:
                min_move = min(min_move, dfs(screen + copy, copy))
            return min_move + 1
        return dfs(1,0)

        