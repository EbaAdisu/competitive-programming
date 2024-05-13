# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
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
        