class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums): return [-1,-1]
        l = 0
        r = len(nums)-1
        mid = (l+r) // 2
        while l <= r:
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
            mid = (l+r) // 2

        if l == len(nums) or nums[l]!=target: return [-1,-1]
        ans = [l,l]
        r = len(nums)-1
        mid = (l+r) // 2
        while l <= r:
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            mid = (l+r) // 2
        ans[1] = r
        return ans