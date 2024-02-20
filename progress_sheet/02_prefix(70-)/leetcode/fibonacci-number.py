class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def fib(n):
            if n < 2:
                return n
            if n in cache:
                return cache[n]
            left = fib(n-2)
            right = fib(n-1)
            cache[n] = left+right
            return cache[n]
        return fib(n)