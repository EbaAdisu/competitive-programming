class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            e = nums[i]
            while l < r:
                su = e + nums[l] + nums[r]
                if su > target:
                    r -= 1
                elif su < target:
                    l += 1
                else:
                    return target
                if abs(target - ans) > abs(target - su):
                    ans = su
        return ans

