# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        # l = n.bit_length()
        ans = 0
        for i in range(32):
            k1 = 1<<i
            k2 = 1<<(31-i)
            if k1 & n:
                ans |= k2
            else:
                ans &= ~k2
        return ans

        