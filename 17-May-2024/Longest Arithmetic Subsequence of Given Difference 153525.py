# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        pre = defaultdict(int)
        for e in arr:
            pre[e] = pre[e - difference] + 1
        ans = 0
        for e in pre:
            ans = max(ans, pre[e])
        return ans
