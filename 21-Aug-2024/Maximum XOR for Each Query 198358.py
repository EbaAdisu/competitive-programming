# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        N = len(nums)
        k = (1<<maximumBit) - 1
        xor = 0
        for num in nums:
            xor ^= num
        ans = []
        for ind in range(N-1,-1,-1):
            ans.append(xor ^ k)
            xor ^= nums[ind]
        return ans
        