# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cache = {}
        def trade(i,buy):
            if i >= len(prices):
                return 0
            if (i,buy) in cache:
                return cache[(i,buy)]
            max_profit = trade(i+1, buy)
            if buy:
                max_profit = max(max_profit, trade(i+1, 0) - prices[i])
            else:
                max_profit = max(max_profit, trade(i+1, 1) + prices[i] - fee)
            cache[(i,buy)] = max_profit
            return max_profit
        return trade(0,1)
