# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window =defaultdict(int)
        l = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in window and window[s[r]] >= l :
                l = window[s[r]]+1
            window[s[r]] = r
            ans = max(ans, r-l+1)
        return ans



        