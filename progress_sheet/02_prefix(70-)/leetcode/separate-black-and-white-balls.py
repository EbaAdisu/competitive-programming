class Solution:
    def minimumSteps(self, s: str) -> int:
        black = 0
        ans = 0
        for r, e in enumerate(s):
            if e == '0':
                ans += r - black
                black+=1
        return ans
            

