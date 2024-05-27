# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        N = len(stones) 
        target = stones[-1]
        check = set(stones)
        dp = {stone:set() for stone in stones}
        dp[0].add(0)
        for stone in stones:
            for k in dp[stone]:
                if k>0 and stone + k in dp:
                    if stone + k == target:
                        return True
                    dp[stone+k].add(k)
                if k >-1 and stone + k+1 in dp:
                    if stone + k + 1 == target:
                        return True
                    dp[stone+k+1].add(k+1)
                if k >1 and stone + k-1 in dp:
                    if stone + k - 1 == target:
                        return True
                    dp[stone+k-1].add(k-1)
        return len(dp[stone]) > 0



