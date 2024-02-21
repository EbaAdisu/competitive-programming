class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        pre = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            div = ceil(nums[i] / pre)
            pre = nums[i]//(div)
            ans += div - 1
        return ans
