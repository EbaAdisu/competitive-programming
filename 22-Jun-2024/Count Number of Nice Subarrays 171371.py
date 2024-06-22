# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre_ks = Counter()
        pre_ks[0] = 1
        odd_count = 0
        ans = 0
        for num in nums:
            if num%2:
                odd_count += 1
            ans += pre_ks[odd_count - k]
            pre_ks[odd_count] += 1
        return ans