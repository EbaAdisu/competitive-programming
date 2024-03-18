class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target: return len(nums)
        if nums[0] > target: return 0
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l