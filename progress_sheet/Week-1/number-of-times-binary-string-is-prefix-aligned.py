class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        pre = 0
        ans = 0

        for i, e in enumerate(flips):

            if e > pre:
                pre = e 
            if pre == i+1:
                ans += 1

        return ans
        