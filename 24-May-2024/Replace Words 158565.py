# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = defaultdict(int)
        def insert(trie, word):
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = defaultdict(int)
                cur = cur[char]
            cur['is_end'] = True
        def root_word(trie, word):
            cur = trie
            root = ''
            for char in word:
                if cur['is_end']:
                    break
                if char not in cur:
                    return word
                root += char
                cur = cur[char]
            return root
        for word in dictionary:
            insert(trie, word)
        root_sentence = []
        for word in sentence.split():
            root_sentence.append(root_word(trie, word))
        return ' '.join(root_sentence)

        