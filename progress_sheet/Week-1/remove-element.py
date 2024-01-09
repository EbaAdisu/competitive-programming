class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = len(nums)-1
        t = 0
        for i in range(len(nums)):
            if nums[-i-1] == val:
                nums[-i-1],nums[pos] = nums[pos], nums[-i-1]
                pos -= 1
                t += 1
        return len(nums) - t