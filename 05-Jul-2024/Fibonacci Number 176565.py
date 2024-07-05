# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        pre,ppre = 1,0
        for i in range(n):
            pre, ppre = pre + ppre, pre
        return ppre
        