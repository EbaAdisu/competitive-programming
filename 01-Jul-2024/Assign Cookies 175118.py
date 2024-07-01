# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        for ind in range(len(s)):
            if s[ind] >= g[child]:
                child += 1
                if child == len(g):
                    break
        return child

        