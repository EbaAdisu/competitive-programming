class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        t = 0
        for i in range(0,len(s),k):
            if t%2:
                ans += s[i:i+k]

            else:
                ans += s[i:i+k][::-1]

            t+=1

        return ans