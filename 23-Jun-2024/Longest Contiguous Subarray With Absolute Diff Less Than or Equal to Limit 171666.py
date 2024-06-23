# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        min_que = deque()
        max_que = deque()
        l = 0
        ans = 0
        for ind in range(N):
            while min_que and min_que[-1] > nums[ind]:
                min_que.pop()
            while max_que and max_que[-1] < nums[ind]:
                max_que.pop()
            min_que.append(nums[ind])
            max_que.append(nums[ind])
            while max_que[0] - min_que[0] > limit:
                if max_que[0] == nums[l]:
                    max_que.popleft()
                if min_que[0] == nums[l]:
                    min_que.popleft()
                l += 1
            ans = max(ans, ind - l + 1)
        return ans