# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dp(index, stoke, k):
            if index >= len(prices) or k <= 0:
                return 0
            if (index, stoke, k) in cache:
                return cache[(index,stoke,k)] 
            passing = dp(index + 1, stoke, k)
            if stoke:
                selling = dp(index + 1, not stoke, k-1) + prices[index]
                cache[(index,stoke,k)] = max(selling, passing)
            else:
                buying = dp(index + 1, not stoke,k) - prices[index]
                cache[(index,stoke,k)] = max(buying, passing)
            return cache[(index,stoke,k)]
        return dp(0, False, 2)
                
            


        