class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        ans=0
        se=set()
        for e in num: 
            if e in se:continue 
            l=e
            r=e
            while l-1 in num:
                l-=1
                se.add(l)
            while r+1 in num:
                r+=1
                se.add(r)
            se.add(e)
            ans=max(ans,r-l+1)
            if ans>len(num)-len(se):
                break
            # print(e,num )
        return ans 