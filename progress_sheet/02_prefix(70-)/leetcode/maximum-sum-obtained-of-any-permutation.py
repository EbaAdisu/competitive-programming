class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre = [0 ] * (len(nums)+1)
        for l,r in requests:
            pre[l] += 1
            pre[r+1] -= 1
        for i in range(1,len(pre)):
            pre[i] += pre[i-1] 
        pre = sorted(pre[:-1], reverse = True)
        nums.sort(reverse = True)
        ans = 0
        for i in range(len(pre)):
            ans += nums[i] * pre[i]
            if pre[i] == 0:
                break
        return ans % (10**9 + 7)