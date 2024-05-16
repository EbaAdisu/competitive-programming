# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        l = 0 
        r = len(nums) - 1
        while l < r:
            su = nums[l] + nums[r]
            if su > k:
                r -= 1
            elif su < k:
                l += 1
            elif su == k:
                ans += 1
                l+=1
                r-=1
        return ans