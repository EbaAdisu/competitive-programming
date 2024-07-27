# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        post = nums[::]
        pos = 1
        for ind in range(N-1, -1,-1):
            post[ind] = pos
            pos *= nums[ind]
        ans = []
        pre = 1
        for ind in range(N):
            ans.append(pre * post[ind])
            pre *= nums[ind]
        # print(post)
        return ans 
        