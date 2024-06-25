# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        nums = sorted(zip(difficulty,profit))
        difficulty = [e[0] for e in nums]
        profit = [e[1] for e in nums]
        worker.sort()
        # print()
        N, M = len(worker), len(profit)
        maxi_so_far = 0
        l = 0
        ans = 0
        for ind in range(N):
            while l < M and difficulty[l] <= worker[ind]:
                maxi_so_far = max(maxi_so_far, profit[l])
                l += 1
            ans += maxi_so_far
        return ans

        