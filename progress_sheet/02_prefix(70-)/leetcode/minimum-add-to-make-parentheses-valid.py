class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        closed = 0
        for e in s:
            if e ==')':
                if opened:
                    opened -= 1
                else:
                    closed += 1
            else:
                opened += 1
        return opened + closed

