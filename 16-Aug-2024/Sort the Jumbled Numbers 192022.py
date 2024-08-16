# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def val(num):
            new_num = 0
            for n in str(num):
                new_num = new_num*10 + mapping[int(n)]
            return new_num
        N = len(nums)
        nums = [(nums[ind], ind ) for ind in range(N)]
        nums.sort(key = lambda x: (val(x[0]),x[1]))
        nums = [num[0] for num in nums]
        return nums
        