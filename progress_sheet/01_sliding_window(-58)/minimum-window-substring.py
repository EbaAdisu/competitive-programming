class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isin(c1,c2):
            for k in c1:
                if c1[k] > c2[k]:
                    return False
            return True
        c1 = Counter(t)
        c2 = Counter()
        l = 0
        ans = []
        for r, e in enumerate(s):
            c2[e] += 1
            while isin(c1, c2):
                if ans and  r-l+1 < ans[1]-ans[0]:
                    ans = [l,r+1]
                elif not ans:
                    ans = [l,r+1]
                c2[s[l]] -= 1
                l+=1
                # print(c2,l ,ans)
        if ans :
            return s[ans[0]:ans[1]]
        return ''
