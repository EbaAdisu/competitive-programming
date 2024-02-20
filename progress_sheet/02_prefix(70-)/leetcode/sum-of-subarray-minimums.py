class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr + [0]
        stack = []
        ans = 0
        for r, e in enumerate(arr):
            while stack and stack[-1][1] > e:
                p, v = stack.pop()
                ans += ((p - stack[-1][0]) * (r-p))*v
            stack += [(r,e)]
        return ans%(10**9 + 7)
        