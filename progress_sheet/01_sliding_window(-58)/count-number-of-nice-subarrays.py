class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        l = 0
        ans = 0
        odd = 0
        for r, e in enumerate(nums):
            if e%2:
                odd += 1
            ans += count[odd - k]
            count[odd] += 1
            
        return ans

