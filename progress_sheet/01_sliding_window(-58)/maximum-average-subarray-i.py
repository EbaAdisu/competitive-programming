class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        ans = window_sum / k
        for i in range(len(nums)-k):
            window_sum += nums[i + k] - nums[i]
            ans = max(ans, window_sum / k)
        return ans