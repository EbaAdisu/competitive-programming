class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            e = nums[i]
            while l < r:
                su = e + nums[l] + nums[r]
                if su > 0:
                    r -= 1
                elif su < 0:
                    l += 1
                else:
                    ans.add((e,nums[l],nums[r]))
                    r -= 1
                    l += 1
        return ans

