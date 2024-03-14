class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = 0
        r = len(citations) - 1

        while l <= r:
            mid = (l+r)//2
            if citations[mid] >= (n - mid):
                r = mid - 1
            else:
                l = mid + 1
            # print(mid,(l,r))
        return n - l
        