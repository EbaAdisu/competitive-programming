# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        trie = defaultdict(int)
        def insert(word):
            print(word)
            cur = trie
            for char in word:
                cur['count'] += 1
                if char not in cur:
                    cur[char] = defaultdict(int)
                print(char, cur['count'])
                cur = cur[char]
            cur['count'] += 1
            print(char, cur['count'])

        for word in strs:
            if not word:
                return ""
            insert(word)
        ans = ''
        cur = trie
        while len(cur) == 2:
            # print([e for e in cur], cur['count'])
            char = [e for e in cur if e != 'count'][0]
            if cur[char]['count'] != N:
                break
            # print(char)
            ans += char
            cur = cur[char]
        return ans
        