class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(l,r):
            mid = (l+r) // 2
            while l < r:
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
                mid = (l+r) // 2
            return mid if nums[mid] == target else -1

        l = 0
        r = len(nums) - 1
        mid = (l+r) // 2
        while l < r:
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
            mid = (l+r) // 2
        print(mid)            
        if nums[-1] >= target:
            return binary(mid,len(nums)-1)
        return binary(0,mid-1)
        
        
        
            

        