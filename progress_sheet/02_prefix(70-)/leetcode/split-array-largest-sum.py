class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def validator(weight):
            part = 1
            presum = 0
            for e in nums:
                presum += e
                if presum > weight:
                    part += 1
                    presum = e
            return part <= k
        l = max(nums)
        r = sum(nums)
        while l <= r:
            mid = (l + r) // 2
            if validator(mid):
                r = mid - 1  
            else:
                l = mid + 1
        return l