class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = None
        l = 0

        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero != None:
                    l = zero + 1
                    zero = i
                else:
                    zero = i

            ans = max(ans, i - l)

            # print(ans,zero,l,i)
        return ans

        