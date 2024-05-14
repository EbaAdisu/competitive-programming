# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        cache = {}
        # @lru_cache
        def dp(i, amount):
            if amount == 0:
                return 1
            if amount < 0 or i >= len(coins):
                return 0
            if (i,amount) in cache:
                return cache[(i,amount)]
            max_way = dp(i+1,amount)
            k = 1
            while k * coins[i] <= amount:
                max_way += dp(i+1, amount - coins[i] * k)
                k += 1
            cache[(i,amount)] = max_way
            return max_way
        return dp(0, amount)