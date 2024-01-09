class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        fir = sec = 0
        while fir < len(g) and sec < len(s):
            if g[fir] <= s[sec]:
                fir += 1                
            sec += 1
        return fir
        