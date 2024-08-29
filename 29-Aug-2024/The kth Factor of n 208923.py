# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
    
        for e in range(1,n+1):
            if n % e == 0:
                k -= 1
                if k == 0:
                    return e

        return -1