# https://atcoder.jp/contests/dp/tasks
from collections import Counter, defaultdict, deque


def inbound(r, c):
    if 0 <= r < m and 0 <= c < n:
        return dp[r][c]
    return 0


s = input()
t = input()
m, n = len(s), len(t)
dp = [[[0]] * n for i in range(m)]
for r in range(m):
    for c in range(n):
        if s[r] == t[c]:
            dp[r][c] = inbound(r-1, c-1) + 1
        else:
            maxi = max(inbound(r-1, c), inbound(r, c-1))
            dp[r][c] = maxi
ans = ''
r, c = m-1, n-1
while inbound(r, c):
    if s[r] == t[c]:
        ans += s[r]
        r, c = r - 1, c-1
    else:
        maxi = max((inbound(r, c-1), (r, c-1)), (inbound(r-1, c), (r-1, c)))
        r, c = maxi[1]
print(ans[::-1])
