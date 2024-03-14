class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validator(weight):
            part = 1
            presum = 0
            for e in weights:
                presum += e
                if presum > weight:
                    part += 1
                    presum = e
            return part <= days
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = (l + r) // 2
            if validator(mid):
                r = mid - 1  
            else:
                l = mid + 1
        return l