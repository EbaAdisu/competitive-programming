# Problem: They Are Everywhere - https://codeforces.com/problemset/problem/701/C

from collections import Counter
n = int(input())
s = input()
total = len(Counter(s))
window = Counter()
l = 0
ans = n
for r in range(n):
    window[s[r]] += 1
    while total == len(window) and window[s[l]] > 1:
        window[s[l]] -= 1
        l += 1
    if total == len(window):
        ans = min(ans, r - l + 1)
print(ans)
