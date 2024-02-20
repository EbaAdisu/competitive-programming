class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even = n//2
        odd = n - even
        def recur(e,n):
            if n == 0: return 1
            if n == 1:
                return e
            return (((recur(e,n//2)%mod)**2)%mod * recur(e,n%2))%mod
        return (recur(4,even) * recur(5,odd))%mod