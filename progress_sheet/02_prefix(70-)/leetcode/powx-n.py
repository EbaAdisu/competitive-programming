class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        elif n < 0:
            return self.myPow(1/x,-n)
        return self.myPow(x,n//2) ** 2 * self.myPow(x,n%2)