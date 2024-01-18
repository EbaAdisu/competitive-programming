class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        a="abcdefghijklmnopqrstuvwxyz"
        pre = [0] * (len(s)+1)

        for l, r, v in shifts:
            pre[l] += 1 if v == 1 else -1
            pre[r+1] -= 1 if v == 1 else -1

        s = list(s)
        s[0] = a[(a.index(s[0])+pre[0])%26]
        for i in range(1,len(pre)-1):
            pre[i] += pre[i-1]
            pos = (a.index(s[i])+pre[i])%26
            s[i] = a[pos]
        return ''.join(s)
        