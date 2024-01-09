class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix=0
        l=0
        ans=len(nums)+1
        for i,e in enumerate(nums):
            prefix+=e
            while l<=i and prefix>=target:
                ans=min(ans,i-l+1)
                prefix-=nums[l]
                l+=1
        return 0 if ans==len(nums)+1 else ans 