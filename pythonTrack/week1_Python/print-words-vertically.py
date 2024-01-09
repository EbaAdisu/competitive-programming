class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans=[]
        l=0
        for e in s.split():
            if len(e)>l:
                l=len(e)
        for i in range(l):
            col=''
            for e in s.split():
                if i<len(e):
                    col+=e[i]
                else:
                    col+=' '
            r=len(col)-1
            while col[r]==' ':
                r-=1
            ans+=[col[:r+1]]
        return ans

        