class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        ans = 0
        pre = float('-inf')
        for l,r in points:
            if l > pre:
                ans += 1
                pre = r
        return ans

        