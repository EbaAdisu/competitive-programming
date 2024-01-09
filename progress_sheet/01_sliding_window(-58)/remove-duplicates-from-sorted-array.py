class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hold = 1

        for r in  range(1,len(nums)):
            if nums[r] != nums[hold - 1]:
                nums[hold], nums[r] = nums[r], nums[hold]
                hold += 1

        return hold
        