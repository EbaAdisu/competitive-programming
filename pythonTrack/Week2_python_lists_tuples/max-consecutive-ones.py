class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        t=0
        ans=0
        for e in nums:
            if e==1:
                t+=1
                ans=max(t,ans)
            else:
                t=0
        return ans