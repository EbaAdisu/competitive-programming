n, k = map(int, input().split())
arr = sorted(map(int, input().split()))
# 1 means wins
# 0 means lose

# bottom up
dp = [0] * (k + 1)
for i in range(k+1):
    for num in arr:
        if i >= num:
            dp[i] = max(dp[i], 1-dp[i - num])
# print(dp[-1])
if dp[-1]:
    print('First')
else:
    print('Second')


# Top Down

def dfs(k):
    if k < 0:
        return 1

    ret = 0
    for e in arr:
        ret = max(1-dfs(k-e), ret)
    # print(k, ret)
    return ret


# print(dfs(k))
