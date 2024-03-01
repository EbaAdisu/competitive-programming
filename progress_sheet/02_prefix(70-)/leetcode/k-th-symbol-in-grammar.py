class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recur(n,k):
            if n == 1:
                return '0'
            ans = '01' if recur(n-1,k//2) =='0' else '10'
            return ans[(k)%len(ans)]
        return int(recur(n,k-1))
