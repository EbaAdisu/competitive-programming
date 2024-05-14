# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        @lru_cache
        def max_product(n):
            if n == 1:
                return 1
            max_next = 0
            for i in range(1,n):
                max_next = max(max_next, max_product(n-i) * i, (n-i) * i)
            # print(n, max_next)
            return max_next
        return max_product(n)
        