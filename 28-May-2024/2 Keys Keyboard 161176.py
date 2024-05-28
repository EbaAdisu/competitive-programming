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
        dp = [[float('inf')]*(n+1) for i in range(n+1)]
        dp[1][0] = 0

        for r in range(1, n + 1):
            ans = float('inf')
            for c in range(r+1):
                ans = min(ans, dp[r][c])
                if r >= c:
                    dp[r][r] = min(dp[r][r], dp[r][c] + 1)
                    if r + c <= n:
                        dp[r + c][c] = min(dp[r + c][c], dp[r][c] + 1)
        return ans



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

        