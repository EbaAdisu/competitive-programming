# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            y = find(y)
            x = find(x)
            if x == y:
                return -1
            if size[x] >= size[y]:
                parent[y] = parent[x]
            else:
                parent[x] = parent[y]
        parent = {p:p for p in range(n)}
        size = {p:0 for p in range(n)}

        ans = [False for i in range(len(queries))]
        queries = sorted([(queries[i][0], queries[i][1], queries[i][2], i) for i in range(len(queries))], key = lambda x: x[2])
        edgeList.sort(key = lambda x: x[2])
        s = 0

        for f in range(len(queries)):
            a,b,d,i = queries[f]
            while s < len(edgeList) and edgeList[s][2] < d:
                x, y, _ = edgeList[s]
                union(x,y)
                s += 1
            ans[i] = find(a) == find(b)
            
        return ans



        