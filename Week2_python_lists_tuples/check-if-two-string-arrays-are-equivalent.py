class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1=''
        for e in word1:
            s1+=e
        s2=''
        for e in word2:
            s2+=e
        return s1==s2