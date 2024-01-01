class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        ans = 0
        print(piles)
        for i in range(n//3, n,2):
            ans += piles[i]
        return ans
        