class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=str()
        ind=0
        while ind<len(word1) or ind<len(word2):
            if ind<len(word1)and ind<len(word2):
                merged+=word1[ind]+word2[ind]
            elif ind<len(word1):
                merged+=word1[ind]
            else:
                merged+=word2[ind]
            ind+=1
        return merged