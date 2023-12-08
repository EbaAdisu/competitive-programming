class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        su=(n)*(n+1)/2
        return int(su-sum(nums))