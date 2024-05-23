# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        trie = defaultdict(int)
        def insert(word):
            cur = trie
            for char in word:
                cur['count'] += 1
                if char not in cur:
                    cur[char] = defaultdict(int)
                cur = cur[char]
            cur['count'] += 1
        

        for word in strs:
            if not word:
                return ""
            insert(word)
        ans = ''
        cur = trie
        while len(cur) == 2:
            char = [e for e in cur if e != 'count'][0]
            if cur[char]['count'] != N:
                break
            ans += char
            cur = cur[char]
        return ans
        