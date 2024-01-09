class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = l = 0
        r = len(nums) - 1
        while l < r:
            su = nums[l] + nums[r] 
            if su >= target:
                r -= 1
            else :
                ans += r - l
                l += 1
        return ans
            