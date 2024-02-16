class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQue = deque()
        maxQue = deque()
        l = 0
        ans = 0
        for r, e in enumerate(nums):
            while maxQue and maxQue[-1] < e:
                maxQue.pop()
            maxQue.append(e)
            while minQue and minQue[-1] > e:
                minQue.pop()
            minQue.append(e)

            while maxQue[0] - minQue[0] > limit:
                p = nums[l]
                l += 1
                if p == maxQue[0]:
                    maxQue.popleft()
                if p == minQue[0]:
                    minQue.popleft()
            ans = max(ans,r-l+1)
        return ans


        