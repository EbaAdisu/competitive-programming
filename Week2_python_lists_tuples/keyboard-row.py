class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1="qwertyuiop"
        s2="asdfghjkl"
        s3="zxcvbnm"
        def wordins(w,s):
            w=w.lower()
            for e in w:
                if e not in s:
                    return False
            return True 
        ans=[]
        for w in words:
            if wordins(w,s1):
                ans+=[w]
            elif wordins(w,s2):
                ans+=[w]
            elif wordins(w,s3):
                ans+=[w]
        return ans