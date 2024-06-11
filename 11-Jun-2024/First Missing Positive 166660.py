# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for ind, num in enumerate(nums):
            while 1 <= num <= N and nums[num-1] != num:
                nums[ind], nums[num-1] = nums[num-1], nums[ind]
                num = nums[ind]
            # print(nums)
        for ind in range(N):
            if nums[ind] != ind + 1:
                return ind + 1
        return N + 1
