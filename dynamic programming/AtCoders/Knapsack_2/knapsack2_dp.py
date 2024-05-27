# https://atcoder.jp/contests/dp/tasks


n, weight = map(int, input().split())
arr = []
max_val = 0
ans = 0
for _ in range(n):
    w, v = map(int, input().split())
    ans = max(v, ans)
    max_val += v
    arr.append([w, v])
arr.sort()

vals = [[float('inf'), set()]] * (max_val + 1)
vals[0] = [0, set()]
for val in range(1, max_val + 1):
    min_w = vals[val]
    for i, (w, v) in enumerate(arr):
        if val - v >= 0 and i not in vals[val-v][1]:
            min_w = min([w + vals[val-v][0], set([i]) | vals[val-v][1]], min_w)
    vals[val] = min_w

for val in range(1, max_val + 1):
    if vals[val][0] <= weight:
        ans = val

print(ans)
