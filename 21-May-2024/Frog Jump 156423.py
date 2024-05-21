# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        stones = set(stones)
        def valid(new_val, val):
            return new_val in stones and new_val > val

        dp = {}
        def dfs(val, k):
            # print(val, k)
            if val == target:
                return True
            if (val, k) in dp:
                return dp[(val,k)]
            ans = False
            if valid(val + k + 1, val):
                ans = ans or dfs(val +  k + 1, k+1)
            if valid(val + k , val):
                ans = ans or dfs(val +  k , k)
            if valid(val + k - 1,val ):
                ans = ans or dfs(val +  k - 1, k-1)
            dp[(val, k)] = ans
            return dp[(val, k)]
        # ret = dfs(0, 0)
        # print(ret)
        return dfs(0, 0)
