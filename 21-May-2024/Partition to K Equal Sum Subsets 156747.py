# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if sum(nums)%k:
            return False
        seen = (1<<(n))-1
        target = sum(nums)//k
        print(sum(nums), target)
        @cache
        def dfs(num, seen):
            # print(num, bin(seen))
            if seen == 0:
                return num == target
                # print(seen)
            elif num > target:
                return False
            if num == target:
                num = 0
            for i in range(n):
                if (seen & (1 << i)):
                    if dfs(num + nums[i], seen^1<<i):
                        return True
            return False
        # return False
        return dfs(0,seen)
        