class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        l = 1
        r = x//2
        while l < r:
            mid = (l + r + 1) // 2
            if mid ** 2 == x:
                return mid
            elif mid **2 > x:
                r = mid - 1
            else:
                l = mid
        return l
            