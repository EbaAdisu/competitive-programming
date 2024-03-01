class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1.0:
            return True
        if n>2:return self.isPowerOfThree(n/3)
        return False 
        