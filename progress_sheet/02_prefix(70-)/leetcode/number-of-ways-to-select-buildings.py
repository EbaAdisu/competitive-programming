class Solution:
    def numberOfWays(self, s: str) -> int:
        pre0 = [0] *len(s) 
        post0 = [0] *len(s) 
        post1 = [0] *len(s) 
        pre1 = [0] *len(s) 
        for i in range(len(s)):
            if s[i] == '0':
                pre0[i] = 1
            else:
                pre1[i] = 1
            if i > 0:
                pre1[i] += pre1[i-1]
                pre0[i] += pre0[i-1]
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                post0[i] = 1
            else:
                post1[i] = 1
            if i < len(s) -1:
                post1[i] += post1[i+1]
                post0[i] += post0[i+1]

        ans = 0
        for i in range(len(s)):
            if s[i] == '0':
                ans += pre1[i] * post1[i]
            else:
                ans += pre0[i] * post0[i]

        return ans


 
