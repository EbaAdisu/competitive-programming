# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        pre = 0
        post = sum(nums)
        for ind in range(N):
            post -= nums[ind]
            if pre == post:
                return ind
            pre += nums[ind]
        return -1
        