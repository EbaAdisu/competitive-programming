# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

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
    if size[x] == size[y]:
        parent[y] = parent[x]
        size[x] += 1
    if size[x] > size[y]:
        parent[y] = parent[x]
    else:
        parent[x] = parent[y]
 
 
 
n, m, k = map(int, input().split())
parent = {p: p for p in range(1, n + 1)}
size = {p: 0 for p in range(1, n+1)}
for _ in range(m):
    s = input()
stack = []
for _ in range(k):
    stack.append(input().split())
ans = []
while stack:
    op, a, b = stack.pop()
    x, y = int(a), int(b)
    if op == 'ask':
        ans.append('YES' if find(x) == find(y) else 'NO')
    else:
        union(x, y)
while ans:
    print(ans.pop())