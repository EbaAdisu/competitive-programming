# Problem: Interesting drink - https://codeforces.com/problemset/problem/706/B/

from bisect import bisect_left, bisect_right
n = int(input())
nums = sorted(map(int, input().split()))

t = int(input())
for _ in range(t):
    m = int(input())
    print(bisect_right(nums, m))
