class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validator(k):
            hours = 0
            for e in piles:
                hours += ceil(e/k)
            return hours <= h
        l = 1
        r = max(piles) * len(piles)
        while l < r:
            mid = (l+r)//2
            if validator(mid):
                r = mid
            else:
                l = mid + 1
            # print(mid,(l,r))
        return r
        