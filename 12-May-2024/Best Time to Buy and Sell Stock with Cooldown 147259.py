# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        cache = {}
        def profit(i,buy):
            if i >= len(prices):
                return 0
            if (i,buy) in cache:
                return cache[(i,buy)]
            max_profit = profit(i+1,buy)
            if buy:
                max_profit = max(max_profit, profit(i+1,0) - prices[i])
            else:
                max_profit = max(max_profit, profit(i+2,1) + prices[i])
            cache[(i,buy)] = max_profit
            # print(i,buy, max_profit)
            return max_profit
        return profit(0,1)