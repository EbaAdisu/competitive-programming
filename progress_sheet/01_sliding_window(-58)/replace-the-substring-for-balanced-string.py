class Solution:
    def balancedString(self, s: str) -> int:
        def isin(c1,c2):
            for k in c1:
                if c1[k] > c2[k]:
                    return False
            return True
        count = Counter(s)
        req = Counter()
        n = len(s)//4
        for k in count:
            req[k] = max(0,count[k]-n)

        print(count,req, isin(count,req))
        # sliding window
        l = 0
        count = Counter()
        ans = len(s)+1
        for r,e in enumerate(s):
            count[e]+=1
            while l<=r and isin(req,count):
                ans = min(ans,r-l+1)
                count[s[l]]-=1
                l+=1
            if isin(req,count):
                ans = min(ans,r-l+1)

        return ans
