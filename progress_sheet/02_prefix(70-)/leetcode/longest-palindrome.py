class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        odd = sum([1 for e in Counter(s).values() if e%2])
        n -= odd
        if odd>0:
            n += 1
        return n

        