# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic={heights[i]:names[i] for i in range(len(names))}
        ans=[]
        for i in sorted(heights,reverse =True ):
            ans+=[dic[i]]
        return ans 

