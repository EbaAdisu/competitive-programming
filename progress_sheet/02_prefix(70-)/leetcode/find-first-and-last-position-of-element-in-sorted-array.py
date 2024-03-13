class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums): return [-1,-1]
        l = 0
        right = len(nums)-1
        r = right
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] >= target:
                right = mid if nums[mid] > target else right
                r = mid - 1
            else:
                l = mid + 1

        if l == len(nums) or nums[l]!=target: return [-1,-1]

        ans = [l,l]
        r = right
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        ans[1] = r
        return ans