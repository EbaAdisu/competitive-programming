class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newn = sorted(nums)
        pos = {newn[i] : i for i in range(len(nums)-1,-1,-1)}
        for i in range(len(nums)):
            nums[i] = pos[nums[i]]
        return nums

        