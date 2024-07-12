# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def redix(nums,n):
            if len(nums) < 2 or n == 0:
                return nums
            count = [[] for i in range(10)]
            for num in nums:
                count[((num)//n)%10].append(num)
            ans = []
            for backet in count:
                ans.extend(redix(backet,n//10))
            # print(count, n, ans)
            return ans
        sorted_num = redix(nums,10**9)
        ans = 0
        for ind in range(1,len(sorted_num)):
            ans = max(ans, sorted_num[ind] - sorted_num[ind-1])
        # print(sorted_num)
        return ans