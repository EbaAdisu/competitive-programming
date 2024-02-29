class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ''
        def nice(s):
            nonlocal ans
            if not s: return
            part = []
            for i, e in enumerate(s):
                if e.isupper():
                    if e.lower() not in s:
                        part += [i]
                else:
                    if e.upper() not in s:
                        part += [i]
            if not part:
                if len(s) > len(ans):
                    ans = s
                return 

            part += [len(s)]
            l = 0
            for i in part:
                nice(s[l:i])
                l = i + 1
        nice(s)
        return ans