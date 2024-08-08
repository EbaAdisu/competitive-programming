# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for ind in range(N-1):
            if nums[ind] == nums[ind+1]:
                nums[ind] = nums[ind+1]*2
                nums[ind + 1] = 0
        zero = 0
        for ind in range(N):
            if nums[zero] == 0:
                nums.append(nums.pop(zero))
            else:
                zero += 1                
        # print(nums)
        return nums
        