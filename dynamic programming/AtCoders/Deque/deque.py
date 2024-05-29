n = int(input())
nums = list(map(int, input().split()))

# bottom up
dp = [[0] * n for i in range(n)]
for l in range(n):
    for r in range(n-l):
        # print((r, r+l), end=' ')
        if l == 0:
            dp[r][r] = nums[r]
        else:
            dp[r][r+l] = max(nums[r+l] - dp[r][r+l-1],
                             nums[r] - dp[r + 1][r+l])
    # print()
# for i in dp:
#     print(i)

print(dp[0][-1])

# top down
cache = {}


def dfs(l, r):
    # print(l, r)
    if l == r:
        return nums[l]
    if (l, r) in cache:
        return cache[(l, r)]
    cache[(l, r)] = max(nums[l]-dfs(l+1, r), nums[r]-dfs(l, r-1))
    return cache[(l, r)]


# print(dfs(0, n-1))
