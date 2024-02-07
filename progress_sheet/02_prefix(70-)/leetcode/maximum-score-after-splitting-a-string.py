class Solution:
    def maxScore(self, s: str) -> int:
        ones = sum(map(int, [e for e in s]))
        zeros = 0
        ans = 0
        for e in s[:-1]:
            if e == '0':
                zeros += 1
            else:
                ones -= 1 
            print(zeros,ones)
            ans = max(ans,ones+zeros)
        return ans
        