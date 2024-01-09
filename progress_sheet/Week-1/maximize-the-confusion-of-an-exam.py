class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = {'T':0,'F':0}
        ans = 0
        l = 0

        for r, e in enumerate(answerKey):
            count[e]+=1
            while count['F'] > k and count['T'] > k:
                count[answerKey[l]] -= 1
                l += 1
            ans = max(ans,r-l+1)

        return ans
        