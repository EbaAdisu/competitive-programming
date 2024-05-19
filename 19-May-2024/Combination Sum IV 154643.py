# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0]=1
        for i in range(1, target+1):
            for j in range(len(nums)):
                if i -nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]
        return dp[-1]
        cache = {}
        def backtrack(num):
            if num == target:
                return 1
            if num > target:
                return 0
            if num in cache:
                return cache[num]
            total = 0
            for i in range(len(nums)):
                num += nums[i]
                total += backtrack(num)
                num-=nums[i]
            cache[num] = total 
            return cache[num]
        return backtrack(0)