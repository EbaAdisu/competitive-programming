class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        pos={nums[i]:i for i in range(len(nums))}
        for o,n in operations:
            pos[n]=pos[o]
            nums[pos[o]]=n 
            pos.pop(o)
        return nums 