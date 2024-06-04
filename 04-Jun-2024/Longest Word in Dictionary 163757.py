# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        stack = []
        ans = ''
        for word in sorted(words):
            while stack and len(stack[-1]) >= len(word):
                stack.pop()
                
            if (not stack and len(word) == 1) or ( stack and stack[-1] == word[:-1]):
                stack.append(word)
                if len(word) > len(ans):
                    ans = word
        return ans