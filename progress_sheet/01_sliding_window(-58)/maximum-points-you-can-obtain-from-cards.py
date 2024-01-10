class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window = sum(cardPoints[:-k])
        ans = total - window
        d = n - k

        for r in range(d,n):
            window += cardPoints[r]
            window -= cardPoints[r - d]

            ans = max(ans,total - window)
        return ans