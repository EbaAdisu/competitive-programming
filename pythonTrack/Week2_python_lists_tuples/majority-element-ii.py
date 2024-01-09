class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        for e in nums:
            if e not in ans and nums.count(e)>len(nums)/3:
                ans+=[e]
        return ans