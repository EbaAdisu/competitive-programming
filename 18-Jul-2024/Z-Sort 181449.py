# Problem: Z-Sort - https://codeforces.com/problemset/problem/652/B

n = int(input())
nums = sorted(map(int, input().split()), reverse=True)
evens = nums[:n//2]
odds = nums[n//2:]
# print(odds)
# print(evens)
for i in range(n):
    if (i+1) % 2:
        nums[i] = odds[i//2]
    else:
        nums[i] = evens[i//2]
print(*nums)
