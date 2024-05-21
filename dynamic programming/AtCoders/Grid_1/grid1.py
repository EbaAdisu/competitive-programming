# https://atcoder.jp/contests/dp/tasks
mod = 10**9+7
m, n = map(int, input().split())
pre = [0] * n
pre[0] = 1
for _ in range(m):
    row = input()
    dp = [0] * n
    for i in range(n):
        if row[i] == '.':
            dp[i] += pre[i]
            if i > 0:
                dp[i] += dp[i-1]
    pre = dp
print(dp[-1] % mod)
