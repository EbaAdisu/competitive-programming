class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        pre = 0
        for i in range(len(nums)):
            e = nums[i]
            pre += e
            ans = max(ans, ceil(pre/(i+1)))
        return ans
        