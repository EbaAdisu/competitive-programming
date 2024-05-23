# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.root = defaultdict(int)

        

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur:
                cur[ch] = defaultdict(int)
            cur = cur[ch]
        cur['is_end'] = True        

    def search(self, word: str) -> bool:
        cur = self.root
        def dfs(cur, i):
            if i == len(word):
                # print(cur)
                return  cur['is_end'] == True
            result = False
            if word[i] == '.':
                for char in cur:
                    if char != 'is_end':
                        result |= dfs(cur[char], i + 1)
            elif word[i] in cur:
                result |= dfs(cur[word[i]], i + 1)
            return result
        return dfs(cur,0)
 
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)