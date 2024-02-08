class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        ans = nums[0]
        for i in range(len(nums)):
            pre += nums[i]
            ans = max(ans,pre)
            if pre < 0:
                pre = 0
        return ans