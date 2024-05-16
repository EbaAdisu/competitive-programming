# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1 = [0]*len(prices)
        dp2 = [0]*len(prices)
        l = prices[0]
        mp = 0
        for r, e in enumerate(prices):
            if e < l:
                l = e
            mp = max(e-l, mp)
            dp1[r] = mp
        r = prices[-1]
        mp = 0
        for l in range(len(prices)-1,-1,-1):
            e = prices[l]
            if e > r:
                r = e
            mp = max(r-e, mp)
            dp2[l] = mp
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, dp1[i] + dp2[i])
        return ans
        