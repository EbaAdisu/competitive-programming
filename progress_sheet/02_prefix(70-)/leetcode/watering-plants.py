class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans=0
        c=capacity
        for i,e in enumerate(plants):
            if c>=e:
                ans+=1
                c-=e
            else:
                ans+=i*2+1
                c=capacity-e
        return ans
        