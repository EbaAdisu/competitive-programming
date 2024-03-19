class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        ans = 0
        pre = 0
        for r, e in enumerate(nums):
            if nums[0] + e > target:break
            l = pre

            while l >= 0 and nums[l] + e > target:
                l -= 1

            if l == r:
                pre = r + 1
            else:
                pre = l

            ans += pow(2,r,mod)#2**(r)%mod
            if r != l:
                ans -= pow(2,r-l-1,mod) #(2 ** (r-l-1))%mod
            ans%= mod
        return ans % mod
        