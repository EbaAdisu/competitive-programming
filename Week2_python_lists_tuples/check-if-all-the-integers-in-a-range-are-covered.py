class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        setOfNums = {i for i in range(left,right+1)}
        for l,r in ranges:
            for j in range(l,r+1):
                setOfNums.discard(j)
            if len( setOfNums) == 0:
                return True
        return len( setOfNums) == 0