# Problem: Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = defaultdict(int)
        for ind, word in enumerate(words):
            self.insert(word, ind)
    def insert(self, word, ind):
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = defaultdict(int)
            cur = cur[char]
        cur['ind'] = ind

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for char in pref:
            if char not in cur:
                return -1
            cur = cur[char]
        posi = []
        def dfs(cur, word):
            if word[-len(suff):] == suff and 'ind' in cur:
                posi.append(cur['ind'])
            for char in cur:
                if char != 'ind':
                    dfs(cur[char], word + char)
        dfs(cur, pref)
        if posi:
            return max(posi)
        return -1
            
    
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)