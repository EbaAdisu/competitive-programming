from collections import *
for i in range(int(input())):
    n = int(input())
    arr = list(map(int,list(input())))
    prefix = defaultdict(int)
    prefix[0] = 1
    pre = 0
    ans = 0
    for r, e in enumerate(arr):
        pre += e
        ans += prefix[pre - r - 1]
        prefix[pre - r - 1] += 1
    print(ans)