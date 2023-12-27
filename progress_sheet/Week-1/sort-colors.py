class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        t = 0
        while 0 in count:
            nums[t] = 0
            t += 1
            count[0] -= 1
            if count[0] == 0:
                count.pop(0)
        while 1 in count:
            nums[t] = 1
            t += 1
            count[1] -= 1
            if count[1] == 0:
                count.pop(1)
        while 2 in count:
            nums[t] = 2
            t += 1
            count[2] -= 1
            if count[2] == 0:
                count.pop(2)
        