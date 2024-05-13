# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        cache = {}
        def subseq(i,j):
            if i >= m or j >= n:
                return 0
            if (i, j) in cache:
                return cache[(i,j)]
            not_pick = max(subseq(i + 1, j), subseq(i, j+1))
            pick = 0
            if text1[i] == text2[j]:
                pick = subseq(i+1,j+1) + 1
            max_sub = max(not_pick, pick)
            # print(i,j,max_sub)
            cache[(i,j)] = max_sub
            return max_sub
        return subseq(0,0)

        