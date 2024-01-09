class Solution:
    def freqAlphabets(self, s: str) -> str:
        alph='abcdefghijklmnopqrstuvwxyz'
        pos={str(i+1):alph[i] for i in range(26)}
        ans=''
        i=len(s)-1
        while i>=0:
            if s[i]=='#':
                ans+=pos[s[i-2:i]]
                i-=2
            else:
                ans+=pos[s[i]]
            i-=1
        return ans[::-1]