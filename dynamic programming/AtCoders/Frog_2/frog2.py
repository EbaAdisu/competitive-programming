def inb(i, j):
    if j >= n:
        return float('inf')
    return abs(arr[i] - arr[j]) + dp[j]


n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * n
for i in range(n-2, -1, -1):
    mini = float('inf')
    for j in range(1, k+1):
        mini = min(mini, inb(i, i+j))
    dp[i] = mini
print(dp[0])
