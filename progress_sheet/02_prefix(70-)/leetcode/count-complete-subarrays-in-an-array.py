class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = Counter(nums)
        window = Counter()
        ans = 0
        l = 0
        for i, e in enumerate(nums):
            window[e] += 1
            while  len(window) == len(count):
                ans += len(nums) - i
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    window.pop(nums[l])
                l += 1
                
        return ans
        