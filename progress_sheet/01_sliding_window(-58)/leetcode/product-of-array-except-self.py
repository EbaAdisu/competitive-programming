class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = [1] * len(nums)
        pos = 1
        for i in range(len(nums)-1, -1 ,-1):
            post[i] = pos
            pos *= nums[i]
        pre = 1
        for i in range(len(nums)):
            post[i] *= pre
            pre *= nums[i]
        return post
            