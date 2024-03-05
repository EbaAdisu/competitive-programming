class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights += [float('-inf')]
        ans = 0
        l = 0
        for i,e in enumerate(heights):
            pre = float('inf')
            l = i
            while stack and stack[-1][0] > e:
                poped,pos = stack.pop()
                ans = max(ans, poped* (i - pos))  
                l = pos              
            stack.append((e,l))
            # print(stack)
        return ans