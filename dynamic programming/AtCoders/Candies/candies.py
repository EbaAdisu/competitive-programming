def prefix(arr):
    p = arr[:]
    for i in range(1, len(arr)):
        p[i] += p[i-1]
        p[i] %= mod
    return p + [0]


mod = 10**9+7


n, k = map(int, input().split())
nums = list(map(int, input().split()))
# bottom up

dp = [0]*(k+1)
dp[0] = 1
for ind, num in enumerate(nums):
    ndp = [0] * (k+1)
    pdp = prefix(dp)
    for i in range(k+1):
        # we can make this a prefix sum
        ndp[i] = (pdp[i] - pdp[max(-1, i-num-1)]) % mod
        # for t in range(min(i+1, num+1)): # this can be made into a prefix sum
        #     if i >= t:
        #         ndp[i] += dp[i-t]
    dp = ndp
print(dp[-1])

# top down
cache = [[-1] * (k+1) for i in range(n+1)]


def dfs(ind, k):
    if ind == n:
        return max(0, 1-k)
    if (ind, k) in cache:
        return cache[(ind, k)]
    if cache[ind][k] != -1:
        return cache[ind][k]
    total = 0

    t = 0
    while t <= k and t <= nums[ind]:
        total += dfs(ind+1, k-t)
        t += 1
    cache[ind][k] = total % mod
    return cache[ind][k]


# print(dfs(0, k))
