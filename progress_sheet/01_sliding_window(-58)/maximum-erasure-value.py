class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        su = 0
        l = 0
        count = defaultdict(int)
        ans = 0
        for r, e in enumerate(nums):
            count[e] += 1
            su += e
            while count[e] > 1:
                count[nums[l]] -= 1
                su -= nums[l]
                l += 1
            ans = max(ans, su)
        return ans
            

        