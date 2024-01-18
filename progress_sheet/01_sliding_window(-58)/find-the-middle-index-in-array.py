class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        pre = 0
        for i, e in enumerate(nums):
            total -= e
            if total == pre:
                return i
            pre += e
        return -1