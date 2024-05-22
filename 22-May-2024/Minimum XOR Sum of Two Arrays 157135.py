# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        num2 = (1<<n) - 1
        dp = {}
        def dfs(ind,num2):
            if num2 == 0 or ind >= n:
                return 0
            if (ind,num2) in dp:
                return dp[(ind,num2)]
            ans = float('inf')
            for j in range(n):
                if not(num2 & 1<<j):
                    continue
                ret = dfs(ind + 1, num2 ^ 1<<j)
                ans = min(ans,  ret + (nums1[ind] ^ nums2[j]))
            dp[(ind,num2)] = ans
            return ans
        return dfs(0, num2)
        