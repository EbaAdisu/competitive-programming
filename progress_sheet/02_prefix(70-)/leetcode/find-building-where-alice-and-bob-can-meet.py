class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        def leftHeight(stack, val):
            if val >= stack[0][0]:
                return -1
            l = 0 
            r = len(stack) - 1
            while l < r:
                mid = (l+r + 1) // 2
                if stack[mid][0] > val:
                    l = mid
                else:
                    r = mid - 1
            return stack[l][1]


        ans = [-1] * len(queries)
        mono_stack = []
        for r, e in enumerate(queries):
            queries[r].sort()
            queries[r].append(r)
        queries.sort(key = lambda x: (x[1],x[0]), reverse = True)
        # print(queries)
        pre = len(heights) - 1
        for l, r, ind in queries:
            while pre > r:
                while mono_stack and mono_stack[-1][0] <= heights[pre]:
                    mono_stack.pop()
                mono_stack.append((heights[pre],pre))
                pre -= 1

            # print(mono_stack)

            if r == l or heights[l] < heights[r]:
                ans[ind] = r
            else:
                if mono_stack:
                    ans[ind] = leftHeight(mono_stack, heights[l])
            # print(ans)

        return ans