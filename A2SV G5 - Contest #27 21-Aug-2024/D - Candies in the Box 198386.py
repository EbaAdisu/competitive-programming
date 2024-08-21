# Problem: D - Candies in the Box - https://codeforces.com/gym/538762/problem/D

# https://codeforces.com/gym/538762
def valid(temp, k):
    v = 0
    while temp >= 10 and temp >= k:
        v += k
        temp -= k
        if temp >= 10:
            temp -= temp//10
    return 2*(temp + v) >= n


n = int(input())

l = 1
r = n
while l < r:
    m = (l+r)//2
    if valid(n, m):
        r = m
    else:
        l = m + 1
print(r)
