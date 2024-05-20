def inb(i, j):
    if j >= n:
        return float('inf')
    return abs(arr[i] - arr[j]) + dp[j]


n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
for i in range(n-2, -1, -1):
    dp[i] = min(inb(i, i+1), inb(i, i+2))
print(dp[0])
