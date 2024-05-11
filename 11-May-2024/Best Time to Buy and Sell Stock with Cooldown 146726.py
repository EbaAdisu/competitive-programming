# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        new_prices = [(prices[i],i) for i in range(len(prices))]
        graph = defaultdict(list)
        mono_stack = []
        for i in range(len(prices)-1,-1,-1):
            while mono_stack and mono_stack[-1][0] < prices[i]:
                mono_stack.pop()
            graph[i].extend(mono_stack[:])
            mono_stack.append((prices[i],i))
        cache = {}
        def profit(i):
            if i >= len(prices)-1:
                return 0
            if i in cache:
                return cache[i]
            max_profit = profit(i+1)
            for p,j in graph[i]:
                trade = prices[j] - prices[i] + profit(j+2)
                max_profit = max(trade,max_profit)
            cache[i] = max_profit
            return max_profit
        return profit(0)