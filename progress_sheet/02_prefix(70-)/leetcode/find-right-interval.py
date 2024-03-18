class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def leftSmall(val):
            if val > start[-1][0]:
                return -1
            if val < start[0][0]:
                return start[0][1]
            l = 0
            r = len(start) - 1
            while l < r:
                mid = (l+r)//2
                if start[mid][0] >= val:
                    r = mid
                else:
                    l = mid + 1
            return start[r][1]

        start = [(intervals[i][0], i) for i in range(len(intervals))]
        start.sort()
        ans = []
        print(start)
        for l, r in intervals:
            pos = leftSmall(r)
            ans += [pos]
        return ans
