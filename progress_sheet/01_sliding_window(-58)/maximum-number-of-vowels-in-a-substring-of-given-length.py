class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel='aeuio'
        count=0
        for i in range(k):
            if s[i] in vowel:
                count+=1
        maxi=count
        for i in range(k,len(s)):
            if s[i] in vowel:
                count+=1
            if s[i-k] in vowel:
                count-=1
            if count>=k:
                return k
            maxi=max(count,maxi)
        return maxi

