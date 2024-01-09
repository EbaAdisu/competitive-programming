class Solution:
    def romanToInt(self, s: str) -> int:
        sym="IVXLCDM"
        val=[1,5,10,50,100,500,1000]
        conv={sym[i]:val[i] for i in range(7)}
        ans=i=0
        while i<len(s):
            if i<len(s)-1 and conv[s[i]]<conv[s[i+1]]:
                ans+=conv[s[i+1]]-conv[s[i]]
                i+=1
            else:
                ans+=conv[s[i]]
            i+=1
        return ans 
        