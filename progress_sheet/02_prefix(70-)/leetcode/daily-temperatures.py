class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        i = 0
        while i < n:
            e = temperatures[i]
            while stack and e > temperatures[stack[-1]]:
                pos = stack.pop()
                ans[pos] += (i - pos)
            stack += [i]
            i += 1
        return ans
            