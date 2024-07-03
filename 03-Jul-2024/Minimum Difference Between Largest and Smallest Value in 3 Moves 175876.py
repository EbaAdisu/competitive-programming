# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        # print(nums)
        ans = float('inf')
        for i in range(4):
            ans = min(ans, nums[~i] - nums[3 - i])
            # print(i, nums[~i] - nums[3 - i] )
        return ans