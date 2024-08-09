# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            y = find(y)
            x = find(x)
            if x == y:
                return -1
            if rank[x] == rank[y]:
                parent[y] = parent[x]
                rank[x] += 1
            if rank[x] > rank[y]:
                parent[y] = parent[x]
            else:
                parent[x] = parent[y]
        parent = {p: p for p in range(n)}
        rank = {p: 0 for p in range(n)}
        ans = []
        for x,y in requests:
            x = find(x)
            y = find(y)
            check = sorted([x,y])
            bol = True
            for a, b in restrictions:
                if sorted([find(a), find(b)]) == check:
                    bol = False
                    break
            if bol:
                
                union(x,y)
            ans.append(bol)
        return ans
