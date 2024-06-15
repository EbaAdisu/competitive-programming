# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        def sortkey(x):
            return x[1]
        project = list(zip(profits, capital))
        project.sort(key = sortkey)
        l = 0
        heap = []
        for _ in range(k):
            while l < len(project) and project[l][1] <= w:
                heappush(heap, -project[l][0])
                l += 1
            if not heap:
                return w
            w += -heappop(heap)
            
        return w

            