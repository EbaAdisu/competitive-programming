from collections import Counter, defaultdict, deque
n, m = map(int, input().split())
graph = defaultdict(list)
degree = Counter()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1
fringe = [i for i in range(1, n+1) if degree[i] == 0]
topo = []
while fringe:
    topo.extend(fringe)
    new_fringe = []
    for vert in fringe:
        for edge_vert in graph[vert]:
            degree[edge_vert] -= 1
            if degree[edge_vert] == 0:
                new_fringe.append(edge_vert)
    fringe = new_fringe
dp = [0] * (n+1)
ans = 0
while topo:
    vert = topo.pop()
    total = 0
    for edge_vert in graph[vert]:
        total = max(total, dp[edge_vert] + 1)
    dp[vert] = total
    ans = max(ans, dp[vert])
print(ans)
