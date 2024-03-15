def maxSpeed(x):
    max_speed = float('-inf')
    for i in range(n):
        max_speed = max(max_speed, abs(x - road[i]) / time[i])
    return max_speed

n = int(input())
road = list(map(int, input().split()))
time = list(map(int, input().split()))
l = min(road)
r = max(road)
while l + 1e-7< r:
    m = (l+r)/2
    m_speed = maxSpeed(m)
    r_speed = maxSpeed(m + 1e-7)
    l_speed = maxSpeed(m - 1e-7)
    if m_speed < l_speed < r_speed:
        l = m
        break
    elif l_speed < m_speed:
        r = m - 1e-7
    else:
        l = m + 1e-7
print(maxSpeed(l))