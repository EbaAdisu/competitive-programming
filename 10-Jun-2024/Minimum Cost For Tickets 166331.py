# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #Bottom up
        max_day = days[-1]
        N = len(days)
        dp = [0] * (N + 1)
        week = 0
        day = 0
        for ind, day in enumerate(days):
            min_cost = dp[ind-1] + costs[0]
            decr = ind
            while decr >= 0  and days[decr] > day - 7:
                min_cost = min(min_cost, dp[decr-1] + costs[1])
                min_cost = min(min_cost, dp[decr-1] + costs[2])
                decr -= 1
            while decr >= 0  and days[decr] > day - 30:
                min_cost = min(min_cost, dp[decr-1] + costs[2])
                decr -= 1
            dp[ind] = min_cost
        return dp[-2]

        #TopDowm
        @lru_cache
        def travel(i):
            if i >= len(days):
                return 0
            oneday = travel(i + 1) + costs[0]
            j = i
            while j < len(days) and days[j] < days[i] +  7:
                j += 1 
            week = travel(j) + costs[1]
            j = i
            while j < len(days) and days[j] < days[i] +  30:
                j += 1 
            month = travel(j) + costs[2]
            # print(i, min(oneday, week, month))
            return min(oneday, week, month)
        return travel(0)