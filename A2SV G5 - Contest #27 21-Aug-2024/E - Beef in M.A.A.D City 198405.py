# Problem: E - Beef in M.A.A.D City - https://codeforces.com/gym/538762/problem/E

# https://codeforces.com/gym/538762

# when you do topo sort if there is cycle in the graph then the topo wont add it to the list.abs
# so you can determine which nodes are in the cycle and which are not in the cycle
from collections import Counter, defaultdict, deque


def topo(graph, degree):
    fringe = [ind for ind in degree if degree[ind] == 1]
    not_cycle = set()
    while fringe:
        new_fringe = []
        for ind in fringe:
            not_cycle.add(ind)
            for new_ind in graph[ind]:
                degree[new_ind] -= 1
                if degree[new_ind] == 1:
                    new_fringe.append(new_ind)
        fringe = new_fringe
    return not_cycle


def bfs(graph, ind):
    level = [0]*(n+1)
    level[ind] = 0
    fringe = [ind]
    visited = set(fringe)
    l = 1
    while fringe:
        new_fringe = []
        for ind in fringe:
            for new_ind in graph[ind]:
                if new_ind not in visited:
                    visited.add(new_ind)
                    new_fringe.append(new_ind)
                    level[new_ind] = l
        fringe = new_fringe
        l += 1
    return level


def solve_editorial(m, v):
    color = [0 for i in range(n+1)]
    pos = 0
    color[m] = 1
    color[v] = 2
    que = deque()
    que.append(m)
    que.append(v)
    while que:
        size = len(que)
        for i in range(size):
            cur = que.popleft()
            for neigh in graph[cur]:
                if color[neigh] == 0:
                    que.append(neigh)
                    color[neigh] = color[cur]

    pos = 0
    for i in range(len(graph)):
        if i + 1 not in not_cycle and color[i+1] == 2:
            pos = 1
    if pos and v != m:
        print("YES")
    else:
        print("NO")


def solve(kendrick, drake):
    for ind in range(1, n+1):
        if ind not in not_cycle and drake[ind] < kendrick[ind]:
            return 'YES'
    return 'NO'


t = int(input())
for _ in range(t):
    n, k, d = map(int, input().split())
    graph = defaultdict(list)
    degree = Counter()
    for _ in range(n):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        degree[v] += 1
        degree[u] += 1

    not_cycle = topo(graph, degree)
    # print(not_cycle)

    kendrick = bfs(graph, k)
    drake = bfs(graph, d)
    print(solve(kendrick, drake))
