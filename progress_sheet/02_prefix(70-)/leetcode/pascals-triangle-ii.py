class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        li = self.getRow(rowIndex - 1)
        ans = li[::]
        for i in range(1,len(li)):
            ans[i] += li[i-1]
        ans += [1]
        return ans
        