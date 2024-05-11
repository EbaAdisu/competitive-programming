# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def profit(i):
            if i >= len(prices)-1:
                return 0
            if i in cache:
                return cache[i]
            max_profit = 0
            for j in range(i+1,len(prices)):
                trade = prices[j] - prices[i]
                if trade >= 0:
                    trade += profit(j+2)
                max_profit = max(profit(j), trade,max_profit)
            cache[i] = max_profit
            return max_profit
        return profit(0)

            


        