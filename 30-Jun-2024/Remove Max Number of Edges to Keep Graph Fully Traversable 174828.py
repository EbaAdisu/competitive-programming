# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
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


        parent = {p: p for p in range(1,n+1)}
        rank = {p: 0 for p in range(1,n+1)}
        extra = 0
        alice = []
        bob = []
        for t, u, v in edges:
            if t == 1:
                alice.append((u,v))
            elif t == 2:
                bob.append((u,v))
            else:
                if find(u) == find(v):
                    extra += 1
                else:
                    union(u,v)
        copy_parent = {p: find(p) for p in range(1,n+1)}
        copy_rank = {p: rank[p] for p in range(1,n+1)}

        # alice
        for u, v in alice:
            if find(u) == find(v):
                extra += 1
            else:
                union(u,v)
        if len(set([find(p) for p in range(1,n+1)])) != 1:
            return -1
        

        # bob
        parent = {p: copy_parent[p] for p in range(1,n+1)}
        rank = {p: copy_rank[p] for p in range(1,n+1)}
        for u, v in bob:
            if find(u) == find(v):
                extra += 1
            else:
                union(u,v)
        if len(set([find(p) for p in range(1,n+1)])) != 1:
            return -1
        return extra
        
