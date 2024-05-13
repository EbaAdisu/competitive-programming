# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mod = 10**7 + 9
        bitmax = {}
        k = 0
        for i in range(ord('a'), ord('j') + 1):
            bitmax[chr(i)] = 1<<k
            k += 1
        presum = Counter()
        presum[0]=1
        xor = 0
        ans = 0
        for i, e in enumerate(word):
            xor ^= bitmax[e]
            for k in range(11):
                ans += presum[xor ^ 1<<k]
            ans += presum[xor]
            presum[xor] += 1
            # print(ans,presum,bin(xor))
            # print()
        return ans
