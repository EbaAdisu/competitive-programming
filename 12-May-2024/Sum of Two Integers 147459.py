# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        limiter = (1<<32) - 1
        while b & limiter:
            a, b = (a ^ b), ((a & b) << 1)
        if a & 1<<31:
            return -((-a&limiter))
        return a &limiter

        