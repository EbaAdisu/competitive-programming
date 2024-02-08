class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pre = defaultdict(tuple)
        preTemp = [0]*len(nums)
        for i, e in enumerate(nums):
            if e in pre:
                ind, val, prev = pre[e]
                dis = i - ind
                newVal = dis
                dis *= (prev-1)
                newVal += dis + val
                pre[e] = (i, newVal, prev+1)
            else:
                pre[e] = (i, 0, 1)
            preTemp[i] = pre[e][1]

        suff = defaultdict(tuple)
        suffTemp = [0]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            e = nums[i]
            if e in suff:
                ind, val, prev = suff[e]
                dis = ind - i
                newVal = dis
                dis *= (prev-1)
                newVal += dis + val
                suff[e] = (i, newVal, prev+1)
            else:
                suff[e] = (i, 0, 1)
            suffTemp[i] = suff[e][1]
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = preTemp[i] + suffTemp[i]
        return ans
        