class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans = [0] * 1001
        for v, l, r in trips:
            ans[l] += v
            ans[r] -= v
        pre = 0
        for e in ans:
            pre += e
            if pre > capacity: return False
        return True

        