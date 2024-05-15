# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cache = {}
        def dp(ind,l):
            if ind >= n:
                sub = s[l:ind]
                if sub == sub[::-1]:
                    return 0
                return n
            if (ind,l) in cache:
                return cache[(ind, l)]
            min_cut = dp(ind + 1,l)
            sub = s[l:ind]
            if l != ind and sub == sub[::-1]:
                cut = dp(ind + 1, ind) + 1
                min_cut = min(min_cut, cut)
            cache[(ind,l)] = min_cut
            return cache[(ind,l)]
        return dp(0,0)
