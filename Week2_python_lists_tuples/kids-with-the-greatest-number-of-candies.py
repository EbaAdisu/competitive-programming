class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        ans=[]
        for e in candies:
            if e+extraCandies>=maxi:
                ans+=[True]
            else:
                ans+=[False]
        return ans