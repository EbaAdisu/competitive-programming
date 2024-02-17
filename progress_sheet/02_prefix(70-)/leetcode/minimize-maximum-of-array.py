class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        pre = 0
        for i, e in enumerate(nums):
            pre += e
            ans = max(ans, ceil(pre/(i+1)))
        return ans
        