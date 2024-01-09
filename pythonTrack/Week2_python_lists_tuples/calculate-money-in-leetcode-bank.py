class Solution:
    def totalMoney(self, n: int) -> int:
        w=n//7
        d=n%7
        wly=(w**2)*7/2+(28*w)-7*w/2
        dly=(d**2)/2+(w)*d+d/2
        return int(wly+dly)