class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == n or k == 1: return 0

        baseScore = weights[0]+weights[-1]
        scores = []
        for i in range(0,n-1):
            scores.append(weights[i]+weights[i+1])

        scores.sort()
        # print(scores,baseScore)
        k -= 1
        maxScore = baseScore + sum(scores[-k:])
        minScore = baseScore + sum(scores[:k])
        return maxScore - minScore
        