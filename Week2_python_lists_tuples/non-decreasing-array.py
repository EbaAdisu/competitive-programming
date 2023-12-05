class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modify=0
        last_max=[nums[0]]
        for index in range(1,len(nums)):
            if nums[index]<nums[index-1]:
                modify+=1
                if modify==2:return False
                poped=last_max.pop()
                if last_max and last_max[-1]>nums[index]:
                    last_max+=[poped]
                    continue
            else:
                if last_max[-1]>nums[index]:
                    modify+=1
                    if modify==2:return False
            last_max+=[nums[index]]
            
        return True