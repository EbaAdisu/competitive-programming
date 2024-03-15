from bisect import bisect_right
n = int(input())
arr = sorted(map(int, input().split()))
q = int(input())
for i in range(q):
    x = int(input())
    print(bisect_right(arr, x))