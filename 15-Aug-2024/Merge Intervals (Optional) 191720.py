# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
        for l, r in intervals:
            if l > right:
                answer.append([left,right] )
                left = l
            right = max(r,right)
        answer.append([left, right])
        return answer

            