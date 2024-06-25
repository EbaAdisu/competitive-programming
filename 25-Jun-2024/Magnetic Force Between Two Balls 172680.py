# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def valid(mid):
            total = -1
            pre = position[0] - mid 
            for pos in position:
                if pos >= pre + mid:
                    total += 1
                    pre = pos
            return total + 1>= m

        position.sort()
        l = 0 
        r = position[-1] - position[0]
        while l<r:
            mid = (l+r+1)//2
            if valid(mid):
                # print(mid)
                l = mid
            else:
                r = mid -1
        return l


        