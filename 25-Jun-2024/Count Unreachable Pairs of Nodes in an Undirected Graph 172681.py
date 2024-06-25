# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            x = find(x)
            y = find(y)
            if x == y:
                return 
            if rank[x] == rank[y]:
                parent[y] = parent[x]
                rank[x] += 1
            elif rank[x] > rank[y]:
                parent[y] = parent[x]
            else:
                parent[x] = parent[y]
        parent = {p:p for p in range(n)}
        rank = {p:0 for p in range(n)}
        for x,y in edges:
            union(x,y)
        counter = Counter()
        for i in range(n):
            counter[find(i)] += 1
        total_pairs = 0
        presum = 0
        counts = list(counter.values())
        for count in counts:
            total_pairs += (presum * count)
            presum += count
        return total_pairs
