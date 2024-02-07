class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre = nums[::]
        for i in range(1,len(pre)):
            pre[i] += pre[i-1]
        ans = [0]*len(nums)
        for i in range(len(nums)):
            pr = nums[i] * (i+1) - pre[i]
            po = (pre[-1] - pre[i]) - nums[i] * (len(nums) - i -1)
            print(pr,po)
            ans[i] = pr + po
        return ans
        