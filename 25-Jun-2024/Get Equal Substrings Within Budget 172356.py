# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        ans = 0
        l = 0
        window = 0
        for ind in range(N):
            window += abs(ord(s[ind]) - ord(t[ind]))
            while window > maxCost:
                window -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            ans = max(ans, ind - l +1 )
        return ans

        