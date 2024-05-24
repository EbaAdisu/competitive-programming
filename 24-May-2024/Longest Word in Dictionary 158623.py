# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = defaultdict(int)
        trie['is_end'] = True

        def insert(trie, word):
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = defaultdict(int)
                cur = cur[char]
            cur['is_end'] = True

        def dfs(trie):

            results = []
            for char in (trie):
                if char != 'is_end' and trie[char]['is_end']:
                    results.append(char + dfs(trie[char]))
            if not results:
                return ''
            results.sort(key = lambda x: (-len(x), x))
            return results[0]
            
        for word in words:
            insert(trie, word)
        return dfs(trie)
        