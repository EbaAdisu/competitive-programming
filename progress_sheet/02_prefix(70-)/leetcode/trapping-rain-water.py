class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for r, e in enumerate(height):
            depth = 0
            while stack and stack[-1][-1] <=  e:
                p, v = stack.pop()
                if r - p > 1:
                    ans += (r-p-1) * (v-depth)
                depth = v
            if stack:
                p,v = stack[-1]
                if r - p > 1:
                    ans += (r-p-1) * (e-depth)
                depth = v
            stack += [(r,e)]
            # print(stack,ans)
        return ans
        