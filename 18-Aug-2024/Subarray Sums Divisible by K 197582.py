# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mods = Counter()
        mods[0] = 1
        cont_sum = 0
        ans = 0
        for num in nums:
            cont_sum += num
            if cont_sum%k in mods:
                ans += mods[cont_sum%k]
            mods[cont_sum%k] += 1
        return ans

        