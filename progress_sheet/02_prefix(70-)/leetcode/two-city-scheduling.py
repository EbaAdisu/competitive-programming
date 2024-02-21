class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        for i, e in enumerate(sorted(costs, key = lambda x:x[0] - x[1])):
            if i < len(costs)//2:
                ans += e[0]
            else:
                ans += e[1]
        return ans