class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        # print(s)
        ans = [0] * len(s)

        for e in s:
            
            word = e[:-1]
            pos = e[-1]
            ind = int(pos)
            ans[ind - 1] = word

        return ' '.join(ans)
        