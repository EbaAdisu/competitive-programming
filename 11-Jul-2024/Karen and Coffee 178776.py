# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())
pre = [0]*200002
newPre = [0]*200002
for i in  range(n):
    a, b = map(int, input().split())
    pre[a] += 1
    pre[b+1] -= 1
if pre[0] >= k:
    newPre[0] = 1
for i in range(1,200002):
    pre[i] += pre[i-1]
    if pre[i] >= k:
        newPre[i] = 1
for i in range(1,200002):
    newPre[i] += newPre[i-1]
for i in range(q):
    a, b = map(int, input().split())
    print(newPre[b]-newPre[a-1])
    