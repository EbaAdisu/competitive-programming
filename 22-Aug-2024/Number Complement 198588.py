# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        ans  = 0
        for i in range(32):
            if num < 1<<i:
                break
            if not num & 1<<i:
                ans ^= 1<<i
        return ans
        