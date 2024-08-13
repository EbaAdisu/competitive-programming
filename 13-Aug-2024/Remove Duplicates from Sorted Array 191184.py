# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        seen = set()
        while l < len(nums):
            if nums[l] in seen:
                nums.pop(l)
            else:
                seen.add(nums[l])
                l += 1
        return l
        