class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg=[e for e in nums if e<0]
        pos=[e for e in nums if e>0]
        ans=[]
        for i in range(len(pos)):
            ans+=[pos[i]]
            ans+=[neg[i]]
        return ans 