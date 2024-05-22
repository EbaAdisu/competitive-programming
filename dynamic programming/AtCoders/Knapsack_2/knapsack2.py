# https://atcoder.jp/contests/dp/tasks


def pop_weight():
    max_w = float('inf')
    pops = []
    for i in range(len(dp)-1, -1, -1):
        if dp[i][0] >= max_w:
            pops.append(i)
        else:
            max_w = dp[i][0]
    pops.sort()
    while pops:
        dp.pop(pops.pop())


def pop_vals():
    max_val = float('-inf')
    pops = []
    for i in range(len(dp)):
        if dp[i][1] <= max_val:
            pops.append(i)
        else:
            max_val = dp[i][1]
    pops.sort()
    while pops:
        dp.pop(pops.pop())


n, w = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()
dp = []
for weight, val in arr:
    temp = [[weight, val]]
    for pw, pv in dp:
        if pw + weight <= w:
            temp.append([pw + weight, val + pv])
        else:
            break
    dp.extend(temp)
    dp.sort(key=lambda x: x[1])
    pop_weight()
    pop_vals()
    # print(dp)
print(dp[-1][-1])


def time(n):
    t = 0
    for i in range(n+1):
        t += i
        print(t)
    print(t)


# time(100)
