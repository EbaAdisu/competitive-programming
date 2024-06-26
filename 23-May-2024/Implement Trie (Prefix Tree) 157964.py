# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        self.root = defaultdict(int)

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur:
                cur[ch] = defaultdict(int)
            cur = cur[ch]
            cur['prefix'] += 1
        cur['is_end'] = True
        cur['word_end'] += 1

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        return cur['is_end'] == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)