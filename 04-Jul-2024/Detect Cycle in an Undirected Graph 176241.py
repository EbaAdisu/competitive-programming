# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            y = find(y)
            x = find(x)
            if rank[x] == rank[y]:
                parent[y] = parent[x]
                rank[x] += 1
            if rank[x] > rank[y]:
                parent[y] = parent[x]
            else:
                parent[x] = parent[y]
	    parent = {p:p for p in range(V)}
	    rank = {p:0 for p in range(V)}
	    edges = set()
	    for i in range(V):
	        for j in adj[i]:
	            tup = tuple(sorted([j,i]))
	            if tup not in edges:
	                edges.add(tup)
	                x, y = tup
	                if find(x) == find(y):
	                    return True
	   
	                union(x,y)
	    return False

		
	


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends