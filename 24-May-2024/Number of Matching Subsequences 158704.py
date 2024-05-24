# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        N = len(s)
        trie =defaultdict(int)
        def insert(trie, word):
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = defaultdict(int)
                cur = cur[char]
            cur['count'] += 1
        
        def dfs(trie, ind, root_char):
            # print(ind,root_char, [e for e in trie])
            while root_char!= '' and ind<N and s[ind] != root_char:
                ind += 1
            if ind >= N:
                return 0
            count = trie['count']
            for char in trie:
                if char != 'count':
                    count += dfs(trie[char],ind + 1, char)
            return count

        for word in words:
            insert(trie, word)
        return dfs(trie, -1, '')
